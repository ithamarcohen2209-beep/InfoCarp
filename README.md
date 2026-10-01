# InfoCarp — Public Legal & Support Site

This public repository contains the static legal and support pages for **InfoCarp** by **Team carp galilee**.

## Official production application

InfoCarp production: https://infocarp.com

The application itself is maintained separately. This public repository intentionally does **not** contain private application source code, API secrets, credentials, signing keys, Firebase service-account data, SMTP credentials or Supabase privileged keys.

## GitHub Pages

GitHub Pages hosts the public legal/support documents used for distribution and store listings:

- Privacy Policy: https://ithamarcohen2209-beep.github.io/InfoCarp/privacy.html
- Support: https://ithamarcohen2209-beep.github.io/InfoCarp/support.html
- Terms of Use: https://ithamarcohen2209-beep.github.io/InfoCarp/terms.html
- Account deletion: https://ithamarcohen2209-beep.github.io/InfoCarp/account-deletion.html
- Security reporting: https://ithamarcohen2209-beep.github.io/InfoCarp/security.html

The apex domain `infocarp.com` is reserved for the production application and must not be assigned to GitHub Pages. A dedicated subdomain such as `legal.infocarp.com` may be added later if desired.

## Platforms

InfoCarp is maintained for Web, Android and iOS. Legal and support information in this repository should remain consistent with the current production features.

## Security

Never commit secrets, API keys, passwords, private certificates, Android keystores, Apple signing material, Firebase service-account credentials, SMTP credentials or privileged Supabase keys to this repository.

## Support

Team carp galilee  
Email: ithamarcohen2209@gmail.com

## Current application scope

The current InfoCarp application supports email and Google sign-in, personal and group fishing sessions, shared competitions with competition-only Zones/Sectors, competition rosters of up to three active anglers per participating group, catch reporting with photos, sector and bathymetry mapping, rod timers and reminders, activity history with live and post-session Smart Fishing Journal insights, natural-language fishing questions, optional privacy-controlled community intelligence, rankings, statistics, Hall of Fame, multilingual UI, and native push notifications on supported mobile platforms. Fish-photo relevance checks are designed to run locally in the app rather than sending catch photos to an external vision service solely for validation.

The production application remains at `https://infocarp.com`; this public repository remains intentionally limited to legal/support content.

## October 2026 feature notes

Measured bathymetry supports interactive terrain, top view, contours and depth profiles; it does not invent depths outside the measurement envelope. Competition invitations include Google Calendar templates and ICS export for manual saving; calendar copies do not update automatically. Current explicit profile consent can include eligible historical and future catches in community/Hall sharing, with session/catch exclusions, anonymous photo/name suppression and separate manual Hall controls. Reliable native ICS sharing requires a mobile build containing the updated bridge.
