# website-dev-emil-motion

**Emil Kowalski: Design Engineering and Motion** · 20 skills · part of [website-dev-skills](https://github.com/aiwithrakshi-dev/claude-design-skills)

- **Original author:** Emil Kowalski
- **Original source:** [emilkowalski/skills](https://github.com/emilkowalski/skills)
- **License:** MIT (see `LICENSE` in this folder)
- **Best for:** Polished UI motion, gestures, Apple-style springs and animation reviews.

## Install

- **claude.ai or desktop app:** download [website-dev-emil-motion.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-emil-motion.plugin), then go to Customize > Plugins > Add > Upload plugin.
- **Claude Code (2.1.275 or later):** `/plugin install website-dev-emil-motion --marketplace aiwithrakshi-dev/claude-design-skills`
- **Claude Code (any version):** `claude plugin marketplace add aiwithrakshi-dev/claude-design-skills` then `claude plugin install website-dev-emil-motion@aiwithrakshi`

## Try these prompts

- Animate this dropdown so it opens from the button, feels fast and can be interrupted.
- /review-animations on src/components (finds motion that feels slow or wrong).
- What is the bouncy effect called when a popover opens? (animation-vocabulary)

## Skills in this plugin

| Skill | What it does |
|---|---|
| `animate` | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose, which tool, which… |
| `animate-expo` | Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it animate, which thread it runs on, which… |
| `animation-performance` | Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main thread when the page is busy, and find the cause when an… |
| `animation-vocabulary` | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop in; "the… |
| `apple-design` | Apple's approach to interface design and fluid, physical motion, translated for the web. |
| `ask-emil` | Ask which skill or flow fits your situation. *(run it by name, e.g. `/ask-emil`)* |
| `ask-sonner` | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating, dismissing and persisting… |
| `break-ui` | Try to break a piece of UI by feeding it worst-case data — long names, unbreakable emails, one-letter names, missing fields, huge counts, zero items, long labels,… |
| `choreograph` | Coordinate several elements that animate together — decide what moves, in what order, how much they overlap, and what stays still — so a group reads as one intentional… |
| `emil-design-eng` | Emil Kowalski's design-engineering philosophy for UI polish, component design, animation decisions, and the invisible details that make software feel great. |
| `find-animation-opportunities` | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. |
| `gestures` | Build drag, swipe, and sheet interactions that track the finger 1:1 and stay interruptible. |
| `improve-animations` | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans for other agents (or… |
| `learn-taste` | Turn a session's design corrections into rules, with their why, in DESIGN.md, a project skill, or a lint check. *(run it by name, e.g. `/learn-taste`)* |
| `mobile-native` | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something that feels installed. |
| `pick-ui-library` | Pick the library for a frontend task from a curated list — primitives, toasts, drawers, command menus, OTP, numbers, charts, virtualization, drag and drop, state,… *(run it by name, e.g. `/pick-ui-library`)* |
| `prototype` | Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and promote the one that feels… *(run it by name, e.g. `/prototype`)* |
| `remove-animations` | Find the animations an interface doesn't need and remove them — motion on keyboard actions, high-frequency surfaces, functional data, and decoration with no purpose —… |
| `review-animations` | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. *(run it by name, e.g. `/review-animations`)* |
| `write-swift` | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent, main-actor-by-default, actors, task… |
