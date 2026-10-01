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

Competition management is available from the Home competition card, including sharing, team invitations, sector assignments and live ranking. Participating groups use their own activity-scoped rod timers. The mapping journal lists prior maps within the selected personal or group scope.

The latest mapping implementation adds map-only fullscreen, a collapsible measurement list, touch pan/pinch zoom and measured slope/depression insights. Depressions require surrounding measurements and distant/unmeasured gaps are excluded. Home management also exposes a competitor view and active representatives under each team, with one live ranking in the management overview. Managers operating competitor tools remain limited to their own accepted group's timers.

Competition ranking offers expandable team details and an optional full table, including selected anglers, sector, derived Zone, available Zone beaches, kg average and gap to the previous place. One calendar entry reveals provider choices. The Smart Journal explicitly distinguishes personal fishing history from active competition data. Initial team roster selection can be completed during an active competition; previously selected rosters remain locked after start. Local catch-photo checks examine overlapping regions before rejecting person-with-fish images; photo-specific model accuracy still requires representative image testing.


### Photo and calendar reliability

Catch photos are checked locally, including overlapping regions for a fish held by a person. Failed or stalled library loads can recover on a subsequent attempt. Classification is probabilistic and can still reject valid photos; the original image is needed to investigate a specific rejection.

Competition calendar choices use Google Calendar or an ICS calendar file in the browser/PWA. Direct Apple event editing is implemented in the native iOS source and requires a native build containing that bridge; a Web deployment does not install this native feature. Physical device behavior remains subject to device validation.

## Competition roles and contacts (Web release 177)

Competition judges and active participants are mutually exclusive within the same competition. Judges explicitly provide a contact phone number that is visible to the competition's authorized participants. Deleted competitions do not trigger phone requests. Live ranking expands to the full viewport, with team cards on narrow screens.

Android package prepared: 1.63.0 (version code 65). No prior Google Play publication is assumed.
