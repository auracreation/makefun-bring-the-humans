from html.parser import HTMLParser
from pathlib import Path
import re


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.assets = [], set(), []
        self.in_main, self.main_ids = False, set()
        self.texts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'main':
            self.in_main = True
        if 'id' in attrs:
            self.ids.add(attrs['id'])
            if self.in_main:
                self.main_ids.add(attrs['id'])
        if tag == 'a':
            self.links.append(attrs)
        if tag in ('script', 'img') and attrs.get('src'):
            self.assets.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.assets.append(attrs['href'])

    def handle_endtag(self, tag):
        if tag == 'main':
            self.in_main = False

    def handle_data(self, text):
        self.texts.append(text)


root = Path(__file__).parent
assert (root / 'index.html').exists(), 'The real landing page must exist at the repository root'
page = Page()
page.feed((root / 'index.html').read_text())
text = ' '.join(page.texts)
for required_copy in ['Take on real bounties with AI agents. Submit your work, compete for top ranks, and win USDC rewards.', 'Discover challenges. Build with AI. Compete for rewards.', 'Discover Bounties', 'Build with AI', 'Submit & Compete', 'Win USDC', 'HUMAN IDEAS. AGENT POWER.']:
    assert required_copy in text, 'Missing final-refinement copy: ' + required_copy
assert {'how-title', 'bounties-title', 'final-title'} <= page.main_ids, 'The main landmark must contain every primary section'
primary_css = re.search(r'\.button-primary\{([^}]+)', (root / 'styles.css').read_text())[1]
gradient = re.search(r'linear-gradient\(([^)]+)', primary_css)[1]
for color in re.findall(r'#[0-9a-fA-F]{6}', gradient):
    rgb = [int(color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in rgb]
    luminance = sum(c * weight for c, weight in zip(linear, [.2126, .7152, .0722]))
    assert 1.05 / (luminance + .05) >= 4.5, 'Small white CTA text must meet 4.5:1 contrast at every gradient stop'
ctas = [a for a in page.links if 'data-signup' in a]
assert len(ctas) >= 4, 'Signup should be available at the major decision points'
assert all(a['href'] == 'https://make.fun/r/z1j4n66g' for a in ctas), 'Every signup CTA must retain the verified referral'
for a in page.links:
    href = a.get('href', '')
    assert href and href != '#', 'No dead navigation links'
    if href.startswith('#'):
        assert href[1:] in page.ids, 'Navigation target missing: ' + href
for asset in page.assets:
    assert not asset.startswith('http'), 'Runtime assets should be local'
    assert (root / asset).is_file(), 'Missing asset: ' + asset
assert (root / '.makefun/owner.json').is_file(), 'The approved agent wallet must claim the repository'
assert 'SPDX-License-Identifier: MIT' in (root / 'LICENSE').read_text()
print(f'PASS: {len(ctas)} referral CTAs, {len(page.links)} links, local assets, ownership and license')
