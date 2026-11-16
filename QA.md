# Verification — 16 November 2026

- `python3 check-site.py`: pass. Five signup CTAs retain the exact verified referral URL; all 21 links have destinations; local runtime assets, wallet ownership and MIT license are present. Every primary section is inside the main landmark. Both primary-button gradient stops meet 4.5:1 contrast with white text.
- `node check-interactions.mjs`: pass. Production-script checks cover mobile menu state, the exact clipboard value, and the readable permission-denied fallback.
- `node --check script.js`: pass.
- All ten unique external navigation destinations returned HTTP 200, including each of the three real bounty examples.
- Actual Chrome viewport checks at 1920×1080, 1440×900, 1366×768, 1024×768, 768×1024, 390×844 and 375×812: no horizontal overflow; header CTA in bounds; hero image loaded. The referral strip fits the initial viewport at every tested width of 768px or above. Mobile retains natural scrolling.
- Actual mobile interactions: menu opens; Tab reaches Bounties; Escape closes it and restores focus; choosing How It Works changes the section hash and closes the menu. The browser copy request completed and displayed its accessible success message. The automation browser's isolated clipboard API returned an empty string, so OS clipboard readback was not independently confirmed. A separate data-URL probe was blocked by the browser's URL policy and was not retried.
- Final Lighthouse mobile audit: Performance 90, Accessibility 100, Best Practices 100, SEO 100. Largest Contentful Paint 3.6s, Total Blocking Time 0ms, Speed Index 0.9s; Cumulative Layout Shift 0. These are one local emulated-mobile run, not production or real-device measurements.
- Reduced-motion CSS disables animation/transitions and smooth scrolling. An OS preference toggle was not exercised.
- Independent static review found primary-button contrast and main-landmark coverage issues. Both were reproduced by failing checks, fixed and checked again.
- `ad.png` is the actual final 1440×900 desktop browser render, converted from the browser's JPEG to PNG without changing its contents. The referral code is visible.

## Scope and provenance

The written brief supplied the initial visual direction. The user later attached a reference image and requested a flatter processor facing the viewer from the left; the generated asset and screenshot were revised accordingly. The official press-kit lockup is used unchanged. The double-slash processor motif is a decorative generated asset, not an official make.fun mark. Bounty examples are dated snapshots, with official detail links and no invented activity or earnings claims.

The bounty does not require hosting; the deliverable is the public source repository and screenshot. No hosting account or production deployment is needed to run the page. AI transcripts and signing credentials are kept outside the public repository; the official kit validates the transcript bundle separately before submission.

## Final UI refinement

The hero now uses locally stored Syncopate Bold 700, chosen after actual browser comparisons against Michroma and Audiowide at the same 67px sample size. Headline CSS sizes and the three-line structure are unchanged. The specified hero paragraph, tagline and four journey labels replace their previous versions. Referral text is larger and darker; the glass strip and independent disclosure remain.

The caption previously used 7px absolute positioning, and the large-desktop offset put it over the glass base. It now occupies its own grid row, at 12px on desktop and 9px on mobile, with stronger contrast. Browser measurements at all seven requested sizes show at least 8.8px of clearance from the image; all desktop/tablet captions and referral strips fit their initial viewport. Mobile scrolls naturally. The existing generated centerpiece was not changed during this refinement.

The final browser session reported no console errors. Keyboard/menu/section navigation and the copy success announcement were retested; the interaction self-check also covers clipboard permission denial. Duplicate CSS overrides and an unused coin symbol were removed. Independent static review of this refinement reported no material findings.
