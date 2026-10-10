# InfoCarp — Public Legal & Support Site

Public legal and support information for **InfoCarp**, operated by **Itamar Cohen (individual operator)**. The application is available at https://infocarp.com.

## Publication boundary

This repository intentionally contains the static legal/support site, not the private application source, backend, native projects or operational infrastructure. Do not add credentials, tokens, production configuration, signing material, customer data, internal diagnostics, deployment workflows or backup/recovery material.

## Pages

- [Home](index.html)
- [Privacy Policy](privacy.html)
- [Support](support.html)
- [Terms of Use](terms.html)
- [Account and data deletion](account-deletion.html)
- [Security reporting](security.html)

The corresponding public URLs use `https://ithamarcohen2209-beep.github.io/InfoCarp/`. Keep `infocarp.com` reserved for the application; this repository does not configure that domain.

## Clone, validate and run

Requirements: Git and Python **3.11 or newer**. The site and its build/tests have no third-party runtime dependencies, API keys, environment variables or `.env` files. Pinned optional developer tools in `requirements-dev.txt` provide Python lint and type checking. The site contains no JavaScript or TypeScript; application build/typecheck commands do not apply here.

```sh
git clone https://github.com/ithamarcohen2209-beep/InfoCarp.git
cd InfoCarp
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 -m ruff check scripts tests
python3 -m mypy
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 -m scripts.build
python3 -m http.server 8000 --directory build
```

Open `http://localhost:8000` in your own browser. Stop the server with Ctrl+C. The build copies only the six public HTML pages, stylesheet and logo into `build/`; it does not modify source pages or deploy anything. CI runs the same lint, Python type checking, validation, tests and build, without production credentials or deployment steps.

The validator checks HTML structure, local links/assets, unsafe URL schemes, CSS balance and high-confidence secret patterns. It is an additional safeguard, not a substitute for reviewing disclosure and privacy changes. No `.env.example` is needed because this site consumes no environment variables; never copy the application's environment configuration here.

## Current application features

InfoCarp supports personal and group fishing sessions; shared competitions with managers, judges and competitors; catch reporting and photos; searchable saved fishing locations; activity history and summaries; rod timers/reminders; weather and environmental information; measured sector/depth maps; rankings, statistics and Hall of Fame; and fishing insights, with an assistant where available. The application UI supports Hebrew, English and Russian. Native notifications and file/calendar sharing depend on platform support, permissions and the installed build.

Forecasts include pressure and selectable daily details in a seven-day view. Current group members can finish or delete a teammate’s personal session through permission-checked operations; deleting a session keeps historical catches. Photo updates preserve existing references during normal synchronization, while explicit removal remains supported. Offline cached information may be available on the device and is reconciled when connectivity returns.

Competition features include code/QR invitations, Zones/Sectors, team representatives, up to three active anglers per group, catch review and final-result history. Judge contact numbers are disclosed to authorized competition participants. Competition calendar exports are optional and external calendar copies must be updated manually.

Bathymetry uses saved measurements and does not invent depth outside the measurement envelope. Maps support terrain, contours, profiles, touch controls and fullscreen. Smart Fishing Journal insights distinguish personal history from competition data. Community/Hall sharing is optional, private by default and controlled through consent and per-session/per-catch exclusions; anonymous sharing suppresses identity/photo details as described in the privacy policy.

### Check List and shopping estimates

- Equipment supports quantities, status and one or more people responsible for bringing it.
- Food/shopping is a shared group list, without a “who brings it” assignment.
- Excel import offers editable names, quantities and categories, skips headings/empty rows and merges duplicates without counting the same imported quantity twice.
- Shopping prices use available real retailer catalogs, including Shufersal and Carrefour. Safe approximate matches are labeled **estimated**; stronger matches are **exact**; missing or unsafe matches are **unavailable**, not zero.
- The basket shows a partial estimated total, exact/estimated/unavailable counts and coverage. Quantity and package size are separate; compatible offers are compared rather than assuming the cheapest unrelated item is a match.
- Incomplete baskets cannot be represented as a fully comparable cheapest store. Availability, freshness, units, package sizes and estimated produce weights can affect results. Verify important prices and quantities before purchasing; estimates are not a retailer quotation.

Catch-photo presence checks can send a reduced image to OpenAI. They are probabilistic, and uncertain/unavailable validation does not guarantee the image is accepted. See the privacy policy for external processing and retention limits.

## Version information reviewed on 10 October 2026

- Web source release: **212**.
- Android source/build: **1.69.0**, version code **71**.
- iOS source: **1.61.0**, build **62**.

These are source/build identifiers, not proof of Google Play or App Store publication. See [CHANGELOG.md](CHANGELOG.md) for public-facing changes and [AUDIT.md](AUDIT.md) for the synchronization boundary.

## Contributing and security

Update related support, privacy and terms text when a feature changes user-facing behavior or data handling. Run the documented checks and review every diff before publication. Do not claim successful deployment, legal certification, data recovery or device testing without evidence.

Report security issues privately as described in [SECURITY.md](SECURITY.md). Support: **thecarpgalilee@gmail.com**.
