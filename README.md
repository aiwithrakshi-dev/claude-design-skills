# website-dev-skills

**343 open-source skills that teach Claude to design and build better websites**: design taste, UI polish, UX, animation (GSAP, Framer Motion, Emil Kowalski), 3D and WebGL effects, React components and presentations, packaged as ready-to-install Claude plugins.

![License: MIT](https://img.shields.io/badge/packaging-MIT-green) ![Skills](https://img.shields.io/badge/skills-343-blue) ![Plugins](https://img.shields.io/badge/plugins-15%20%2B%20all--in--one-purple) ![Works with](https://img.shields.io/badge/works%20with-claude.ai%20%7C%20Desktop%20%7C%20Claude%20Code-orange)

Collected, fixed and packaged by **Rakshith** ([@aiwithrakshi.global](https://www.instagram.com/aiwithrakshi.global) · [MyDesignNexus](https://www.instagram.com/mydesignnexus.in)). The skills themselves were written by the authors credited below. Every skill keeps its original open-source license.

---

## Contents

- [What's inside](#whats-inside)
- [Install in 2 minutes](#install-in-2-minutes)
- [How to use the skills](#how-to-use-the-skills)
- [Sample prompts](#sample-prompts)
- [A full example session](#a-full-example-session)
- [Full skill list](#full-skill-list)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Rebuild or contribute](#rebuild-or-contribute)
- [Credits and licenses](#credits-and-licenses)

## What's inside

You can install everything at once with **`website-dev-skills`** (343 skills in one plugin), or pick only the plugins you need.

| Plugin | Skills | Original author | Best for | Download |
|---|---:|---|---|---|
| **website-dev-skills** (all-in-one) | 343 | Everyone below | Everything in this repo, one install | [website-dev-skills.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-skills.plugin) (27 MB) |
| [`website-dev-design-taste`](plugins/website-dev-design-taste) | 1 | Leonxlnx | Landing pages and company sites that must not look AI-generated or templated. | [website-dev-design-taste.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-design-taste.plugin) |
| [`website-dev-emil-motion`](plugins/website-dev-emil-motion) | 20 | Emil Kowalski | Polished UI motion, gestures, Apple-style springs and animation reviews. | [website-dev-emil-motion.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-emil-motion.plugin) |
| [`website-dev-gsap`](plugins/website-dev-gsap) | 8 | GreenSock | Timelines, ScrollTrigger, pinning, SplitText and GSAP in React or Vue. | [website-dev-gsap.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-gsap.plugin) |
| [`website-dev-framer-motion`](plugins/website-dev-framer-motion) | 6 | C-Jeril (kuakua-app) | React animation with motion components, layout animations, gestures and scroll. | [website-dev-framer-motion.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-framer-motion.plugin) |
| [`website-dev-motion-design`](plugins/website-dev-motion-design) | 1 | LottieFiles | Timing, easing and choreography principles for any animation system. | [website-dev-motion-design.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-motion-design.plugin) |
| [`website-dev-ui-polish`](plugins/website-dev-ui-polish) | 11 | Julien Thibeaut (ibelick) | Fast clean-up passes, accessibility fixes, metadata/SEO tags and DESIGN.md files. | [website-dev-ui-polish.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-ui-polish.plugin) |
| [`website-dev-interface-guidelines`](plugins/website-dev-interface-guidelines) | 1 | Vercel Labs | Checking UI code against Vercel's rules for accessibility, forms, focus, motion and performance. | [website-dev-interface-guidelines.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-interface-guidelines.plugin) |
| [`website-dev-ux-product`](plugins/website-dev-ux-product) | 59 | Uxcel Lab | UX audits, component and screen patterns, and product management documents. | [website-dev-ux-product.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-ux-product.plugin) |
| [`website-dev-oil-ui`](plugins/website-dev-oil-ui) | 1 | oil-oil | Exploring three visual directions side by side and reviewing UI with real screenshots. | [website-dev-oil-ui.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-oil-ui.plugin) |
| [`website-dev-stageshow`](plugins/website-dev-stageshow) | 1 | Benji Taylor | Fake-but-real-looking product UI for heroes, feature cards and animated cursor demos. | [website-dev-stageshow.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-stageshow.plugin) |
| [`website-dev-dimensional-drawing`](plugins/website-dev-dimensional-drawing) | 2 | Enes Ozturk | Apple-style monochrome spec sheets of a component, and a motion film of the sheet. | [website-dev-dimensional-drawing.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-dimensional-drawing.plugin) |
| [`website-dev-frontend-slides`](plugins/website-dev-frontend-slides) | 1 | Zara Zhang | Animated HTML presentations, from scratch or converted from PowerPoint. | [website-dev-frontend-slides.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-frontend-slides.plugin) |
| [`website-dev-mengto-collection`](plugins/website-dev-mengto-collection) | 223 | Meng To | Web design systems, scroll storytelling, WebGL/Three.js effects, illustrations, video and game dev. | [website-dev-mengto-collection.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-mengto-collection.plugin) |
| [`website-dev-21st`](plugins/website-dev-21st) | 8 | 21st.dev | Finding, installing and generating React/shadcn components from 21st.dev with the 21st CLI. | [website-dev-21st.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-21st.plugin) |
| [`website-dev-shadcn-mcp`](plugins/website-dev-shadcn-mcp) | MCP | shadcn | Letting Claude browse, search and install shadcn/ui components and registries. | [website-dev-shadcn-mcp.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-shadcn-mcp.plugin) |

> The all-in-one bundle contains every skill but **not** the shadcn connector. Install `website-dev-shadcn-mcp` on its own if you want it (it needs Claude Code or the desktop app).

## Install in 2 minutes

Pick the way that matches where you use Claude. You only need one of them.

### Option 1: claude.ai or the Claude desktop app, by uploading a file (easiest)

1. Download **[website-dev-skills.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-skills.plugin)**, or any single plugin from the table above.
2. Open **[Customize > Plugins](https://claude.ai/customize/plugins)** in claude.ai or the desktop app.
3. Select **Add**, then **Upload plugin**, and choose the file you downloaded.
4. Open the plugin and make sure its toggle is on.
5. Start a new chat and try a prompt from [Sample prompts](#sample-prompts).

The plugin is saved to your account, so it also appears in Cowork and in Claude Code (run `/reload-plugins` there).

### Option 2: claude.ai or the desktop app, as a marketplace (gets updates automatically)

1. Open **[Customize > Plugins](https://claude.ai/customize/plugins)** and select **Add**, then **Add marketplace**.
2. Enter `aiwithrakshi-dev/claude-design-skills` (or `https://github.com/aiwithrakshi-dev/claude-design-skills`).
3. The 15 plugins now appear in your plugin list. Select the ones you want and press **Add**.
4. To get new versions later, select **Check for updates**, or turn on **Sync automatically**.

### Option 3: Claude Code (terminal, VS Code, JetBrains)

On Claude Code 2.1.275 or later, one line installs a plugin straight from this repo:

```bash
/plugin install website-dev-gsap --marketplace aiwithrakshi-dev/claude-design-skills
```

On any version, add the marketplace once, then install what you want:

```bash
claude plugin marketplace add aiwithrakshi-dev/claude-design-skills

# install one plugin
claude plugin install website-dev-gsap@aiwithrakshi

# or install all 15 plugins with the script in this repo
git clone https://github.com/aiwithrakshi-dev/claude-design-skills.git
cd claude-design-skills
bash scripts/install-claude-code.sh                 # macOS, Linux, WSL
powershell -ExecutionPolicy Bypass -File scripts\install-claude-code.ps1   # Windows
```

Inside a Claude Code session you can do the same with `/plugin marketplace add aiwithrakshi-dev/claude-design-skills` and then `/plugin`. To install only a few with the script, name them: `bash scripts/install-claude-code.sh gsap ui-polish design-taste`.

### Option 4: copy single skills by hand

Every skill is a normal folder with a `SKILL.md`. Copy any folder from `plugins/<plugin>/skills/` into `~/.claude/skills/` (Claude Code) or zip it and upload it in **Customize > Skills**.

### Requirements

- A Claude account. Plugins and skills are added from **Customize** on claude.ai and the desktop app, or with Claude Code.
- Some skills write and run code (for example screenshots, checks or builds). They work best in Claude Code or the desktop app, where Claude can use your project folder.
- **website-dev-21st:** Needs a free 21st.dev account: run `npx @21st-dev/cli login` or create an API key at https://21st.dev/mcp.
- **website-dev-shadcn-mcp:** Runs `npx shadcn@latest mcp` locally, so it works in Claude Code and the Claude desktop app on a computer with Node.js 18+. It does not run in the claude.ai web app.

## How to use the skills

You don't need to remember skill names. **Describe the task and Claude loads the right skill by itself.** For example, "add a GSAP scroll animation that pins the hero" loads the GSAP ScrollTrigger skill.

To pick a skill yourself:

- **claude.ai and desktop:** type `/` in the message box, type the plugin or skill name, and select it.
- **Claude Code:** type `/plugin-name:skill-name`, for example `/website-dev-gsap:gsap-scrolltrigger`. If you installed the all-in-one bundle, use `/website-dev-skills:gsap-scrolltrigger`.

A few skills only run when you call them by name, so Claude never starts them on its own. They are marked *run by name* in the [full skill list](#full-skill-list). Examples: `/review-animations`, `/prototype`, `/learn-taste`.

**Tips for the best results**

- Say what you are building and for whom: "a landing page for a dental clinic in Mysuru" works better than "a landing page".
- Name the stack when it matters: plain HTML, React, Next.js, Tailwind, Vue.
- Ask for a review after a build: "now review it with the web interface guidelines" or "run baseline-ui on it".
- Combine skills: design-taste for the look, GSAP or Framer Motion for motion, ui-polish for the final pass.

## Sample prompts

Copy any of these into Claude after installing the matching plugin (or the all-in-one bundle).

### Design Taste (`website-dev-design-taste`)

```text
Build a landing page for a Bengaluru coffee roastery. Use the design-taste-frontend skill and make it feel hand-made, not like a template.
```
```text
Review this hero section and tell me what makes it look AI-generated, then fix it.
```
```text
Redesign my portfolio homepage with one strong idea per section and real photography.
```

### Emil Kowalski: Design Engineering and Motion (`website-dev-emil-motion`)

```text
Animate this dropdown so it opens from the button, feels fast and can be interrupted.
```
```text
/review-animations on src/components (finds motion that feels slow or wrong).
```
```text
What is the bouncy effect called when a popover opens? (animation-vocabulary)
```

### GSAP (official GreenSock skills) (`website-dev-gsap`)

```text
Add a GSAP ScrollTrigger section that pins the product image while three feature cards scroll past.
```
```text
Convert these CSS keyframes into a GSAP timeline with proper cleanup in React (useGSAP).
```
```text
My GSAP animation stutters on mobile. Find the cause and fix it.
```

### Framer Motion (`website-dev-framer-motion`)

```text
Make this React card grid reorder with smooth shared-layout animation (layoutId).
```
```text
Add a scroll-linked progress bar and parallax hero with useScroll and useTransform.
```
```text
Build a swipe-to-dismiss notification with drag constraints.
```

### Motion Design (LottieFiles) (`website-dev-motion-design`)

```text
Design the loading-to-success micro-interaction for a payment button, with timings and easing.
```
```text
Plan the page transition choreography between my list view and detail view.
```
```text
Apply Disney animation principles to this onboarding illustration sequence.
```

### UI Skills (ibelick) (`website-dev-ui-polish`)

```text
Run a baseline-ui pass on this page: fix spacing, hierarchy and typography only.
```
```text
Fix the accessibility problems in this signup form (labels, focus, contrast, errors).
```
```text
Create a DESIGN.md for my website from its current code.
```

### Vercel Web Interface Guidelines (`website-dev-interface-guidelines`)

```text
Review app/page.tsx against the web interface guidelines and list every violation.
```
```text
Check my forms against the guidelines and fix what fails.
```
```text
Audit this navbar for keyboard, focus and touch-target problems.
```

### Uxcel Product and UX Skills (`website-dev-ux-product`)

```text
Do a full design review of this checkout flow (usability, microcopy, dark patterns).
```
```text
Design the pricing page for my SaaS with three plans.
```
```text
Take my app idea from problem statement to a build-ready product spec.
```

### oil-ui (`website-dev-oil-ui`)

```text
Show me three different visual directions for this dashboard as a side-by-side HTML page.
```
```text
Check my page against DESIGN.md and list any conflicts.
```
```text
Refine the visual hierarchy of this settings screen using a real browser screenshot.
```

### Stageshow (faux product UI) (`website-dev-stageshow`)

```text
Make an animated product demo of my invoicing app: a cursor creates an invoice and sends it.
```
```text
Build a bento grid of feature cards with mocked dashboard UI inside each card.
```
```text
Create a hero illustration of a browser window showing my analytics dashboard.
```

### Dimensional Drawing (`website-dev-dimensional-drawing`)

```text
Make a dimensional drawing of my primary button component with all measurements.
```
```text
Create a spec sheet (anatomy drawing) of this pricing card.
```
```text
Turn that drawing into a 10-second motion film.
```

### Frontend Slides (`website-dev-frontend-slides`)

```text
Make a 10-slide animated HTML pitch deck for my AI automation agency.
```
```text
Convert this PPTX into a web presentation with smooth transitions.
```
```text
Help me find a visual style for my conference talk slides.
```

### Meng To Collection (223 skills) (`website-dev-mengto-collection`)

```text
Build a cinematic scroll-storytelling landing page with GSAP and Lenis.
```
```text
Add a liquid-glass refraction effect to these buttons (refract-liquid-glass).
```
```text
Draw a flat vector empty-state illustration of a developer fixing a bug (illustration-flat).
```

### 21st.dev Skills (`website-dev-21st`)

```text
Find a pricing table component on 21st.dev that matches my site and install it.
```
```text
Generate three hero section drafts with 21st AI and give me the code for the best one.
```
```text
Review my navbar and suggest a better 21st.dev component for it.
```

### shadcn/ui MCP connector (`website-dev-shadcn-mcp`)

```text
Using shadcn, add a data table with sorting and pagination to my dashboard.
```
```text
Show me the available shadcn components for forms and install the ones I need.
```
```text
Install the calendar and date-picker components from shadcn.
```

## A full example session

Here is how several skills work together on one real task, a portfolio landing page:

```text
You:    Build a one-page portfolio for a Bengaluru UI designer. Plain HTML, CSS and JS.
        Make it feel premium and hand-made, with a calm entrance animation.
Claude: (loads design-taste-frontend) picks a direction, type scale and palette,
        then builds the page section by section.

You:    Add a scroll animation where the project cards slide in and the hero pins.
Claude: (loads gsap-scrolltrigger and gsap-timeline) adds ScrollTrigger with cleanup
        and a reduced-motion fallback.

You:    Now check it before I publish.
Claude: (loads web-interface-guidelines and fixing-accessibility) lists problems such as
        missing alt text, weak focus states and small touch targets, then fixes them.

You:    /review-animations
Claude: reviews every animation for timing, easing and interruptibility and suggests fixes.
```

## Full skill list

All 343 skills, grouped by plugin. Open a group to see every skill. Full descriptions are in [docs/SKILLS.md](docs/SKILLS.md) and machine-readable data is in [catalog.json](catalog.json).

<details>
<summary><b>website-dev-design-taste</b> · 1 skill · by Leonxlnx</summary>

| Skill | What it does |
|---|---|
| `design-taste-frontend` | tasteskill 2.5.1, the anti-slop frontend skill. |

</details>

<details>
<summary><b>website-dev-emil-motion</b> · 20 skills · by Emil Kowalski</summary>

| Skill | What it does |
|---|---|
| `animate` | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose,… |
| `animate-expo` | Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it animate, which… |
| `animation-performance` | Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main thread when the page is busy, and find the… |
| `animation-vocabulary` | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover… |
| `apple-design` | Apple's approach to interface design and fluid, physical motion, translated for the web. |
| `ask-emil` | Ask which skill or flow fits your situation. *(run by name)* |
| `ask-sonner` | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating,… |
| `break-ui` | Try to break a piece of UI by feeding it worst-case data — long names, unbreakable emails, one-letter names, missing fields, huge counts, zero… |
| `choreograph` | Coordinate several elements that animate together — decide what moves, in what order, how much they overlap, and what stays still — so a group reads… |
| `emil-design-eng` | Emil Kowalski's design-engineering philosophy for UI polish, component design, animation decisions, and the invisible details that make software… |
| `find-animation-opportunities` | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. |
| `gestures` | Build drag, swipe, and sheet interactions that track the finger 1:1 and stay interruptible. |
| `improve-animations` | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans… |
| `learn-taste` | Turn a session's design corrections into rules, with their why, in DESIGN.md, a project skill, or a lint check. *(run by name)* |
| `mobile-native` | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something that feels installed. |
| `pick-ui-library` | Pick the library for a frontend task from a curated list — primitives, toasts, drawers, command menus, OTP, numbers, charts, virtualization, drag… *(run by name)* |
| `prototype` | Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and… *(run by name)* |
| `remove-animations` | Find the animations an interface doesn't need and remove them — motion on keyboard actions, high-frequency surfaces, functional data, and decoration… |
| `review-animations` | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. *(run by name)* |
| `write-swift` | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent,… |

</details>

<details>
<summary><b>website-dev-gsap</b> · 8 skills · by GreenSock</summary>

| Skill | What it does |
|---|---|
| `gsap-core` | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive,… |
| `gsap-frameworks` | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. |
| `gsap-performance` | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. |
| `gsap-plugins` | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText,… |
| `gsap-react` | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. |
| `gsap-scrolltrigger` | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. |
| `gsap-timeline` | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. |
| `gsap-utils` | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. |

</details>

<details>
<summary><b>website-dev-framer-motion</b> · 6 skills · by C-Jeril (kuakua-app)</summary>

| Skill | What it does |
|---|---|
| `framer-motion-core` | Official Framer Motion skill for the core API — motion components, useAnimationState, useTransform, useMotionValue, useSpring. |
| `framer-motion-gestures` | Official Framer Motion skill for gesture animations — drag, pan, tap, hover, focus, touch animations. |
| `framer-motion-layout` | Official Framer Motion skill for layout animations — shared layout transitions, layoutId, exit animations, AnimatePresence. |
| `framer-motion-react` | Official Framer Motion skill for React integration — AnimatePresence, motion components, useAnimation, layout animations. |
| `framer-motion-scroll` | Official Framer Motion skill for scroll-linked animations — useScroll, useTransform, scroll-triggered animations, parallax. |
| `framer-motion-variants` | Official Framer Motion skill for animation variants — state machines, orchestrated animations, stagger, repeat, sequencing. |

</details>

<details>
<summary><b>website-dev-motion-design</b> · 1 skill · by LottieFiles</summary>

| Skill | What it does |
|---|---|
| `motion-design` | Applies motion design principles to create emotionally-driven, technically sound animations and transitions. |

</details>

<details>
<summary><b>website-dev-ui-polish</b> · 11 skills · by Julien Thibeaut (ibelick)</summary>

| Skill | What it does |
|---|---|
| `baseline-ui` | Quickly deslop UI code by fixing spacing, hierarchy, typography, and small layout issues. |
| `component-canvas` | Build a full-screen, interactive canvas to explore existing UI components and their variants with pan and zoom. |
| `create-canvas` | Build a freeform canvas to explore, compare, and iterate on anything. |
| `create-design-md` | Create or update a DESIGN.md from an existing product repository or public website. |
| `device-frames` | Create device-framed screenshots, product images, videos, or live UI mockups. |
| `fixing-accessibility` | Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, and form errors. |
| `fixing-metadata` | Audit and fix HTML metadata including page titles, meta descriptions, canonical URLs, Open Graph tags, Twitter cards, favicons, JSON-LD structured… |
| `fixing-motion-performance` | Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion, and blur effects. |
| `improve-ui` | Audit an existing product surface against its own design evidence, identify verified UI problems, and write self-contained implementation plans for… |
| `photographing-software` | Create photographic images of software — a website or app shown on a real-looking laptop, display, tablet or phone, shot through a camera with depth… |
| `ui-skills-root` | Use before UI-related work to select the smallest useful UI Skills context through the ui-skills CLI. |

</details>

<details>
<summary><b>website-dev-interface-guidelines</b> · 1 skill · by Vercel Labs</summary>

| Skill | What it does |
|---|---|
| `web-interface-guidelines` | Review or build UI against the Vercel Web Interface Guidelines (accessibility, focus states, forms, animation, typography, performance, navigation). |

</details>

<details>
<summary><b>website-dev-ux-product</b> · 59 skills · by Uxcel Lab</summary>

| Skill | What it does |
|---|---|
| `pm-analytics` | Run a product-analytics analysis that produces a decision, not a dashboard — start from the question, pick actionable over vanity metrics, separate… |
| `pm-assumption-rigor-audit` | Run a structured rigor audit on how a team validated (or plans to validate) its assumptions — for a discovery plan, experiment, test, or any "we… |
| `pm-assumption-testing` | Plan how to test the assumptions behind a product idea before building — decompose the idea into its load-bearing beliefs, prioritize the riskiest,… |
| `pm-competitive-analysis` | Produce or critique a competitive/market analysis that yields a strategic edge — not a flat feature table. |
| `pm-decision-quality-audit` | Run a structured quality audit on a product decision or its rationale — a build/buy/sunset/re-platform/pricing call, a decision log, a… |
| `pm-discovery` | Plan or critique a product discovery process — figuring out what to build before building it. |
| `pm-experimentation-ab` | Design or critique an A/B test or controlled product experiment with statistical rigor — pre-registered falsifiable hypothesis, sample-size/power up… |
| `pm-gtm-plan` | Build a go-to-market plan that's a stage-appropriate system — customers, channels, pricing, timing, and partnerships that fit the company's maturity… |
| `pm-idea-to-plan` | Orchestrated, idea-to-plan PM workflow. |
| `pm-okr-metric-validity-audit` | Run a structured validity audit on OKRs, KPIs, North Star Metrics, or any success-metric set. |
| `pm-okrs-kpis` | Write OKRs, KPIs, or a North Star Metric derived from product strategy — or review an existing goal set. |
| `pm-personas-jtbd` | Build or critique an audience-understanding artifact — research-based user personas, a Jobs-to-Be-Done framing, or the choice between them. |
| `pm-prioritization` | Decide what to build first, or critique a prioritization. |
| `pm-prioritization-rigor-audit` | Run a structured rigor audit on prioritization decisions, scored backlogs, RICE/ICE/MoSCoW outputs, or roadmap orderings. |
| `pm-problem-statement` | Write or critique a product problem statement — turning a vague prompt, signal, or feature request into a clear, evidence-grounded, testable… |
| `pm-product-review` | Orchestrated review of a PM artifact (spec, PRD, OKRs, roadmap, prioritization, strategy). |
| `pm-product-spec` | Write a product requirements document (PRD) or spec anchored to a validated problem, with measurable requirements and surfaced risks — or review an… |
| `pm-roadmap` | Create or critique a product roadmap — outcome-oriented, theme-based, confidence-aware (Now-Next-Later) roadmaps tied to strategy, instead of dated… |
| `pm-spec-quality-audit` | Run a structured quality audit on a product spec, PRD, or requirements document. |
| `pm-user-story` | Write or critique a user story — a small unit of user value framed from a real persona's need, not a restated task. |
| `pm-vision-strategy` | Produce or critique a product vision and/or product strategy — an aspirational destination and the deliberate, trade-off-driven choices to reach it… |
| `ux-accessibility-audit` | Run a structured WCAG 2.1 AA accessibility audit on a design, screen, component, or page. |
| `ux-activity-feed` | Design or critique an activity feed / stream — a scannable list of updates where what matters stands out and noise fades. |
| `ux-aesthetics-audit` | Audit the visual quality of a UI against established visual-design principles — hierarchy, emphasis, contrast, spacing, alignment, grouping,… |
| `ux-buttons` | Design or critique UI buttons — pick the right button type for the action's importance, apply sizing/label/state best practices, and gate stylistic… |
| `ux-cards` | Design or critique UI cards — one-topic, scannable cards with clear hierarchy, the right container style (elevated, outlined, flat), and restrained… |
| `ux-checkout-payment` | Design or critique a checkout, cart, payment, or booking flow — the path from "ready to buy" to "order confirmed." Applies the conversion-protecting… |
| `ux-color` | Design or critique a product's color palette and system — base hue, harmony, neutrals, semantic colors, tonal scales, and tokens. |
| `ux-contact-support` | Design or critique a contact/support experience — help center, FAQ, contact methods, live chat, point-of-error help, and feedback flows. |
| `ux-dark-patterns-audit` | Audit a UI, flow, or copy for dark (deceptive) patterns — design that manipulates users into unintended actions. |
| `ux-dashboard` | Design or critique an analytics or data dashboard — which metrics earn a place, how to organize and prioritize them, and which chart fits each one. |
| `ux-design-from-scratch` | Orchestrated, build-from-zero UX workflow. |
| `ux-design-review` | Orchestrated, holistic UX review of a screen, flow, or component. |
| `ux-empty-states` | Design or critique empty states — first-use screens, cleared states, no-results pages, and 404s that explain why the screen is empty and guide the… |
| `ux-error-recovery` | Design or critique how a product prevents, surfaces, and recovers from errors — input/validation errors, system & network failures, AI/prediction… |
| `ux-heuristics-audit` | Run a structured usability audit of any UI against Nielsen's 10 heuristics. |
| `ux-iconography` | Choose and design UI icons that are understood, not just decorative — universal metaphors, one consistent style, text/accessible labels where… |
| `ux-information-architecture-audit` | Run a structured information architecture audit on a sitemap, navigation tree, category structure, menu labels, or multi-screen product. |
| `ux-inputs-and-forms` | Design or critique forms and input fields — field selection, labels, layout, validation, error states, and submission. |
| `ux-landing-page` | Design or critique a landing page — a focused, conversion-oriented page built around a single goal (sign up, buy, book a demo, subscribe). |
| `ux-layout-spacing-grids` | Lay out a screen with disciplined spacing, sizing, and grids — every value on one base unit (8px/4px scale), content aligned to a grid, proximity… |
| `ux-loaders-and-progress` | Design or critique loading states and progress indicators — match the feedback type (spinner, text, determinate bar, skeleton, progress tracker) to… |
| `ux-login-signup` | Design or critique a login / sign-up screen. |
| `ux-menus` | Design or critique UI menus — pick the right menu type (dropdown, cascading, contextual, single/multi-select, search, inline) for the action set,… |
| `ux-microcopy` | Write or improve UX microcopy — button labels, error and empty states, tooltips, form labels, notifications, and confirmations — so it's clear,… |
| `ux-microcopy-audit` | Audit interface copy — labels, buttons, errors, empty states, tooltips, notifications, form hints — against UX-writing standards. |
| `ux-mobile-responsiveness-audit` | Run a structured mobile-responsiveness audit on a design, screen, or component — viewport adaptation and reflow, orientation, touch-target size and… |
| `ux-modals-and-dialogs` | Design or critique modals, dialogs, alerts, popovers, and bottom sheets — gate WHEN interrupting users is justified, then apply dismissal,… |
| `ux-navigation` | Design or critique navigation systems — match the nav pattern (top bar, sidebar, tabs, hamburger, mega menu, bottom nav) to the information… |
| `ux-notifications-and-toasts` | Design or critique notifications — pick the right type (badge, banner, snackbar, toast, alert, push) for the message's urgency, and respect user… |
| `ux-offboarding` | Design or critique an offboarding flow — canceling a subscription, unsubscribing, or deleting an account. |
| `ux-onboarding` | Design or critique a user-onboarding flow — the first-run experience that gets users to value fast. |
| `ux-pricing` | Design or critique a pricing page. |
| `ux-search` | Design or critique search experiences — search input, auto-suggest, results page, filtering/sorting, and zero-results recovery. |
| `ux-selection-controls` | Design or critique selection controls — pick the right control (checkbox, radio button, toggle switch, dropdown, slider, picker) for the choice… |
| `ux-settings` | Design or critique a settings / preferences page — organizing many options without overwhelm, plus the save model (autosave vs. |
| `ux-tables` | Design or critique data tables and lists — scannable structure, alignment rules (left for text, right for numbers), sorting/filtering, row… |
| `ux-tooltips` | Design or critique tooltips and contextual hints — decide when a tooltip clarifies vs. |
| `ux-typography` | Design or critique a product's typography — typeface selection and pairing, type scale, hierarchy, and readability settings (size, line length, line… |

</details>

<details>
<summary><b>website-dev-oil-ui</b> · 1 skill · by oil-oil</summary>

| Skill | What it does |
|---|---|
| `oil-ui` | UI/UX design skill for Claude Code, Cursor, Codex & AI coding agents: design, refine, and review frontend interfaces for websites, apps, dashboards,… |

</details>

<details>
<summary><b>website-dev-stageshow</b> · 1 skill · by Benji Taylor</summary>

| Skill | What it does |
|---|---|
| `stageshow` | Build faux product UI that looks like a real product, as a still illustration or an animated demo with a cursor. |

</details>

<details>
<summary><b>website-dev-dimensional-drawing</b> · 2 skills · by Enes Ozturk</summary>

| Skill | What it does |
|---|---|
| `dimensional-drawing` | Make an Apple-style monochrome dimensional drawing of a UI component or physical product — title-block summary plus one dense drawing sheet with… |
| `dimensional-drawing-motion` | Turn a finished dimensional drawing sheet into a ~10 s Apple-style motion film — lines draw themselves in, the camera pulls back, layers lift into… |

</details>

<details>
<summary><b>website-dev-frontend-slides</b> · 1 skill · by Zara Zhang</summary>

| Skill | What it does |
|---|---|
| `frontend-slides` | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. |

</details>

<details>
<summary><b>website-dev-mengto-collection</b> · 223 skills · by Meng To</summary>

| Skill | What it does |
|---|---|
| `3d-cloth-material` | Build convincing woven cloth in Three.js, with a thread-level weave normal map, sheen and anisotropic highlights, folds that never stretch the… |
| `3d-construction-sequence` | Animate existing Three.js architecture or equipment assembling from a structural wireframe into finished solids. |
| `3d-falling-leaves` | Build recognizable falling leaves in world space using instanced geometry, independent tumble, coupled sideways drift, shared wind, scene occlusion,… |
| `3d-feature-objects` | Build a responsive feature grid with individual lit 3D objects that turn on hover and ease back into their composed poses. |
| `3d-four-seasons` | Add coordinated spring, summer, fall, and winter states to a 3D scene, blending foliage, sunlight, sky, ground materials, snow, and particles… |
| `3d-harbour-water` | Build sheltered waterfronts in Three.js with depth-aware reflections of docks and signs, rain rings, boats that ride the swell, and wakes that… |
| `3d-high-poly-models` | Create or integrate highly detailed 3D models with smooth silhouettes, shaped surfaces, believable bevels, and close-up geometry, then prepare… |
| `3d-high-resolution-textures` | Build sharp, physically coherent high-resolution materials for 3D rendering with appropriate PBR maps, texel density, UV direction, mipmaps,… |
| `3d-kasumidera-ultra-realism` | Build or art-direct walkable Three.js environments in Kasumidera’s painterly ultra-realism style. |
| `3d-metal-material` | Build hyperrealistic PBR metal in Three.js: steel, brass, gold, copper and iron as true conductors (metalness 1, measured F0 tint, no albedo) with… |
| `3d-modular-buildings` | Model human-scale buildings for a real-time 3D environment. |
| `3d-orbit-inspect-demo` | Make a 3D object lean around on hover and open a full inspect view on click. |
| `3d-paper-material` | Build a paper sheet in Three.js that reads as paper up close — washi, cotton rag or kraft with baked fibre and tooth relief, laid and chain lines, a… |
| `3d-retina-resolution` | Render a 3D canvas sharply on Retina and HiDPI displays, including explicit 200 percent resolution, synchronized renderer and post-processing sizes,… |
| `3d-sky-background` | Create a camera-correct sky background for a 3D scene with a procedural atmosphere or panorama, horizon haze, aligned sunlight, and coherent… |
| `3d-sky-rays` | Add sun shafts and crepuscular rays to a Three.js or equivalent 3D scene, using scene occlusion, a projected sun position, controlled foreground… |
| `3d-survey-scan` | Add a replayable world-space survey pulse to an existing Three.js scene. |
| `3d-ultra-realistic-water` | Build an ultra-realistic open ocean in Three.js with a deep-water Gerstner spectrum shaded per pixel from analytic derivatives, each wave faded at… |
| `3d-underwater-god-rays` | Add volumetric underwater god rays to a Three.js scene, marching one drifting swell field along every view ray at half resolution so the light… |
| `3d-virtual-tour` | Build guided and interactive virtual tours through a 3D environment with authored camera paths, room and floor-plan navigation, orbit inspection,… |
| `3d-wood-lighting-scorecard` | Light carved wood in a dark room in three.js, with procedural grain and pores, one warm key through a window, soft shadows that touch, light shafts,… |
| `3d-wood-material` | Build convincing timber for Three.js as one procedural MeshPhysicalMaterial with growth rings, cathedral figure, pores, medullary rays, checks, tool… |
| `add-mouse-driven-orbit` | Add restrained mouse-driven orbit and parallax depth to a Three.js hero by damping one pointer target and splitting it across camera translation,… |
| `add-shader-cursor-trail` | Add the Shaders WebGPU mouse effect used for the Tidal Commons hero: a white twinkling halftone cursor trail driven by ChromaFlow, masked through a… |
| `agency-grid-layout-minimal` | Create a minimal agency design system with a disciplined editorial grid, oversized typography, quiet uppercase utility labels, restrained image… |
| `ambient-section-particles` | Add a restrained particle atmosphere inside one section with configurable shapes, density, gravity, wind, sway, rotation, recycling or settling,… |
| `animate-procedural-birds` | Build and animate a small bird in Three.js with a recognizable species silhouette, folding wings, independent head and tail motion, grounded toes… |
| `animation-on-scroll` | Create an on-scroll animation trigger using IntersectionObserver with Tailwind-friendly animation classes and keyframes. |
| `animation-systems` | Use when designing or implementing product-grade web motion like Stripe, Linear, Apple, and Vercel. |
| `article-prompts-to-skills` | Convert an article, tutorial, or prompt pack into focused reusable AgentSkills, one independent capability per skill, with portable instructions,… |
| `atmosphere-background` | Create a dark atmospheric background with drifting vertical light folds, screen-blended glow, and a concentrated luminous corner or lower-edge bloom. |
| `audit-ai-design-slop` | Audit websites, apps, screenshots, mockups, and design code for harmful AI-design clichés, generic generated defaults, and established UI defects. |
| `audit-reference-originality` | Audit a website or digital experience against its supplied source references for originality and plagiarism risk. |
| `audit-verify-explain-grade-5` | Audit work, verify claims with concrete evidence, and explain the result in simple grade-5 language. |
| `aura-asset-images` | Use when you need high-quality stock-style images from Aura Assets (aura.build/assets) similar to Unsplash for design mockups and marketing:… |
| `author-game-levels` | Author or revise readable, flat-world Three.js game levels. |
| `background-grid-webgl` | Create a perspective WebGL background grid with fading lines, subtle particle haze, slow forward drift, and gentle camera parallax. |
| `beam-glow-states` | Create React loading, processing, selected, current, focus, and pressed states with the border-beam package's animated edge glow. |
| `beautiful-shadows` | Apply exact Tailwind arbitrary shadow utilities for polished, layered neutral elevation. |
| `blue-cloudy-clean-modern` | Create a clean modern design system with a luminous blue sky atmosphere, soft drifting cloud light, minimal white framing, and serene premium… |
| `blue-laser-clean-glass-layout` | Create a clean dark glass layout system with a thin blue laser atmosphere, frosted premium shells, and polished dashboard structure. |
| `book-serif-index` | Create an archival book-reader design system with serif-led pages, mono index navigation, aged paper surfaces, margin notes, and a premium catalog… |
| `bright-green-tech-system-webgl` | Create a bright-green technical design system with structured split layouts, hard-framed dark surfaces, mono utility labels, and a prominent WebGL… |
| `browser-video-recording` | Create polished 60 fps 4:3 4K browser screen-recording style videos from Codex in-app browser captures, with browser-only crop, natural macOS cursor… |
| `build-3d-character-selector` | Make an original 3D cast from identity and full-body references, prepare textured GLBs for the browser, and build a full-body character selection… |
| `build-awwwards-quality-sites` | Art-direct and implement distinctive, motion-rich marketing, editorial, portfolio, and landing websites with original reference-inspired imagery,… |
| `build-daily-inspiration-sites` | Turn a completed daily UI inspiration capture into exactly five original landing-page builds, one per separate Codex task, using Sites. |
| `build-game-audio-feedback` | Design or implement responsive audio feedback for a Three.js or web game. |
| `build-game-camera-controls` | Implement or tune Three.js game cameras. |
| `build-game-changelog` | Design, implement, backfill, audit, and release in-game changelogs with contiguous versioning, deployment provenance, menu-state navigation,… |
| `build-game-inventory` | Build or repair game inventory, loot, equipment, tooltips, drag-and-drop, persistence, and progression systems. |
| `build-game-map-editor` | Build, extend, or audit production-linked browser map editors for Three.js and isometric games. |
| `build-game-monster-system` | Build, integrate, audit, or refactor rigged monsters for Three.js and web action games. |
| `build-hybrid-game-assets` | Plan, create, integrate, or audit a hybrid asset pipeline for a Three.js or web game. |
| `build-interactive-particle-trail` | Build a cursor or touch particle interaction that emits by distance along the traveled segment into a recycled GPU point pool, with optional… |
| `build-isometric-arpg` | Build or extend a playable isometric action RPG in Three.js, React, or similar web technology. |
| `build-lens-raindrops` | Add camera-space water drops, rain on glass and windshield beads that bend the live scene. |
| `build-mobile-threejs-games` | Build, tune, or test a Three.js game for mobile web. |
| `build-point-cloud-scan` | Build animated 3D scans from actual mesh topology in Three.js or WebGL. |
| `build-rigged-game-assets` | Create, integrate, or audit production-ready rigged 3D characters and monsters with a main model, skeleton, animation library, sockets, collision… |
| `build-threejs-enemy-systems` | Build or refactor reusable, data-driven enemy archetype and moveset systems for Three.js action games. |
| `build-threejs-scroll-worlds` | Build rich, scroll-controlled real-time Three.js experiences as one persistent 3D world whose camera, lighting, atmosphere, materials, objects, DOM… |
| `build-ultra-realistic-game-interiors` | Build or refine photoreal, walkable first-person interiors in Three.js. |
| `build-vesperfall-review-assets` | Build truthful Vesperfall asset-library review pairs from transparent PNG references and live Three.js, FBX, or img2threejs models. |
| `build-wireframe-scan-reveal` | Reveal Three.js geometry with an expanding world-space scan whose wire cage leads the solid surface, then burns away. |
| `cinematic-gsap-lenis-motion-system` | Create premium cinematic web motion systems with GSAP, ScrollTrigger, and Lenis. |
| `cinematic-scroll-storytelling` | Create cinematic scroll-driven landing pages with Lenis smooth scrolling, GSAP ScrollTrigger, scroll-linked progression, staggered text reveals,… |
| `clean-minimal-beige-light-mode` | Create a clean minimal beige light-mode design system with warm neutral shells, quiet process grids, restrained accent color, and elegant… |
| `cobejs` | Use when adding a lightweight interactive globe with cobe (canvas setup, markers, interaction, performance, integration with React/Next.js). |
| `codex-gpt-image-2-5-flare` | Generate or edit artwork with built-in Codex image gen, especially transparent PNG ornaments, game sprites, emblems, and UI graphics. |
| `company-logos` | Use Iconify Simple Icons logos (64x64) instead of text logos. |
| `compose-a-woodland-landing-page` | Compose a Sylva-style botanical landing page as a six-chapter field guide, alternating light editorial spreads, dark participation cards and live… |
| `container-lines` | Add vertical container-size guide lines with mini corner squares for precise, structured web layouts. |
| `control-camera-lenses` | Add photographic focal length, sensor fit, subject tracking and depth-aware shallow focus to a Three.js scene. |
| `corner-diagonals` | Apply diagonal-cut corners and chamfered edges to buttons, cards, panels, and container shells. |
| `corner-lasers` | Create a corner-anchored laser composition with thin beams, a bright emitter node, bloom, and atmospheric glow or fog. |
| `create-ai-avatar` | Make an AI avatar of yourself that looks and sounds like you. |
| `create-game-vfx` | Create readable, performance-safe Three.js game visual effects. |
| `css-alpha-masking` | Apply CSS alpha masking with linear-gradient for horizontal or vertical edge fades (mask-image and -webkit-mask-image). |
| `css-border-gradient` | Apply subtle gradient-border treatments for premium web surfaces. |
| `daily-ui-inspiration-capture` | Create a recurring daily UI inspiration capture. |
| `dark-blue-contrasting-clean` | Create a dark-blue clean design system with strong contrast, cobalt gradient feature blocks, crisp framed structure, and restrained premium glow. |
| `dark-glass-clean-layout` | Create a dark glass layout system with frosted premium shells, clean multi-column workspace structure, floating data cards, and restrained… |
| `design-action-combat` | Design, implement, tune, or test readable tactical action combat for web games. |
| `design-first-ui-prompting` | Use when you need design-first, spec-driven, skimmable prompts for UI generation. |
| `design-game-encounters` | Design, implement, tune, or test Three.js action-game encounters. |
| `digital-twin` | Build a digital twin of yourself, meaning photoreal stills of you in your own real room, talking video clips of you, and lines in your own cloned… |
| `dither-ascii-ink-hover` | Reveal warm dither dots and ASCII marks beneath the pointer on an illustration using intersecting CSS masks. |
| `dither-background` | Create a dark monochrome procedural background with enlarged square pixels and visible Bayer-style ordered dithering. |
| `dither-laser-dark-mode` | Create a dark premium design system that combines near-black surfaces, subtle ordered-dither texture, and a thin accent-colored laser atmosphere. |
| `documentary-brutalist-agency` | Create or redesign creative agency, production studio, architecture, culture, and portfolio websites with billboard typography, hard black-and-white… |
| `editorial-portfolio-chapters` | Create or redesign creative-studio, agency, photographer, artist, and portfolio websites where project work leads the story. |
| `editorial-service-booking` | Create or redesign appointment-based service websites for salons, barbers, spas, wellness studios, clinics, and hospitality brands. |
| `editorial-tech` | Blend editorial magazine composition with precision product-tech detailing using asymmetrical grids, cinematic media bands, mono utility labels, and… |
| `elevenlabs-tts` | Generate ElevenLabs text-to-speech audio from scripts or inline text using local voice profiles. |
| `falling-leaves` | Build falling leaves that read as leaves, with each one tumbling on its own axis so it presents a face, thins to an edge, and opens out again, and… |
| `fire-paper-loader` | Build a burning-paper ring loader whose GLSL flame is drawn by a Worker on an OffscreenCanvas started from the head, so a main thread blocked by the… |
| `fire-smoke-skill-vfx` | Build the effects of a fire skill as one visual language in Three.js. |
| `forest-floor-specimen` | Model an animated 3D botanical study with fern fronds, folded pinnae, a moss cushion and grounded stones for a light editorial Journey section. |
| `framed-grid-layout` | Create minimal framed grid layouts with thin visible boundary lines, L-shaped corner brackets, subtle diagonal line texture, and strict section… |
| `framed-tech-dark-border-gradient` | Create a framed dark technical design system with border-gradient shells, asymmetrical grid panels, mono utility labeling, and restrained monochrome… |
| `funky-purple-container-tech` | Create a dark container-led technical design system with fuchsia-purple accents, layered rounded shells, crisp frame lines, and playful futuristic… |
| `game-dev-character-model` | Create a realistic, AAA-looking 3D character model for a game or web scene, from a description or a reference video/image, as a textured, rigged GLB… |
| `game-dev-combat-animation` | Build, fix and review character combat animations (melee strikes, bow shots, spell casts, skills, monster attacks, whole move sets) so they read… |
| `game-dev-combat-skill-polish` | Score a game's combat skills and spells out of 10 with blind judges, then raise the weakest to a bar, for timing and readability (does a skill read… |
| `generate-ledger-logo-register` | Generate a family of original fictional wordmarks on a Seedream contact sheet, extract transparent assets, and present them as a partner or studio… |
| `generate-reference-inspired-brand-worlds` | Generate multiple original brand campaign worlds from a supplied visual reference while controlling how close the new work feels without copying… |
| `genjutsu-scene` | Make a scene of Meng To himself inside any world, saying his line with his own face, voice and mouth, from his HeyGen Avatar 6 twin to Genjutsu. |
| `glass-dark-mode-clock` | Create a dark glass design system with frosted shells, soft beam grids, circular clock-like calibration dials, and precise sci-fi instrument framing. |
| `glass-dark-ui` | Build dark-mode glassmorphism interfaces with readable contrast, frosted surfaces, and gradient borders using a pseudo-element mask. |
| `globe-gl` | Use when implementing globe.gl (Globe.GL) for 3D globe data visualization with WebGL/ThreeJS, including setup, data layers (points, arcs, polygons,… |
| `globe-particles` | Create a globe-like 3D particle visualization with a dense luminous spherical core and thinner orbital ring or flattened disc. |
| `gooey-blob-system` | Create a gooey blob system using SVG filters where multiple shapes merge into a single fluid form. |
| `gradient-border-flashlight` | Add a pointer-driven flashlight across card groups that lights both the surface and the nearest segment of each gradient border, including adjacent… |
| `gsap` | Use when you need to add or debug professional web animations with GSAP (timelines, ScrollTrigger, stagger, transforms) in HTML/CSS/JS/React. |
| `gsap-scrolltrigger-storytelling` | Build cinematic sticky product storytelling with GSAP ScrollTrigger, progressive UI reveals, scroll-synced animation, smooth interpolation, and… |
| `high-contrast-skeuomorphic-clean` | Create a high-contrast clean skeuomorphic design system with molded dark surfaces, crisp light separation, tactile inset depth, and restrained… |
| `horizontal-scroll-scenes` | Build scene-by-scene chapters that advance left to right on one fixed stage while the user scrolls vertically, with native scroll as the only input. |
| `hover-particle-dissolve` | Make a hovered 3D surface break into grains around the actual pointer hit and reassemble when the pointer leaves. |
| `html-demo` | Show an app working on a web page by drawing it live in HTML instead of recording it. |
| `html-explainer-video` | Turn a product, a feature or an idea into a finished one-minute explainer video in any look: a script (hook, benefit, quick tutorial, try it), a… |
| `html-reel` | Turn a tweet, a video, a YouTube video or a landing page into a 9:16 reel (Instagram Reels, TikTok, Shorts) that says what the source says and looks… |
| `html-to-interaction-prompts` | Convert a supplied HTML page or generated HTML reference into a screenshot-backed article containing multiple reusable interaction prompts. |
| `ice-frost-skill-vfx` | Build the effects of an ice and frost skill as one visual language in Three.js. |
| `illustration-bold-pop` | Draws hand-authored SVG spot illustrations in a bold pop-geometric style for design and coding scenes. |
| `illustration-flat` | Draws flat vector illustrations as SVG cards (480x360): slim, long-limbed people acting out one design or coding moment with one hero prop. |
| `illustration-flat-with-black` | Draws flat vector spot illustrations of tall, long-legged people doing design and coding things, with solid black as a main colour. |
| `illustration-framed-panel` | Draws original design-and-coding scenes as SVG cards (480x360) in a framed-panel cartoon style. |
| `illustration-grainy-gouache` | Draws original cosy animal scenes as hand-authored SVG cards (480x360) in a grainy gouache, risograph-like style. |
| `illustration-halftone-line` | Draws hand-authored SVG spot illustrations in a halftone line style for design and coding scenes. |
| `illustration-ink-sketch` | Draws hand-inked cartoon critters and living objects as SVG cards (480x360), each acting out a coding or design idea. |
| `illustration-isometric-mono` | Draws true-isometric diorama illustrations of developer and design workspaces in one green ramp, generated as SVG with a bundled scene kit. |
| `illustration-line-interior` | Draws original hand-written SVG spot scenes in the Line interior style, wide airy rooms or terraces where slim, realistic people do design and… |
| `illustration-one-line` | Draws original hand-written SVG spot illustrations in the One-line style, joyful action figures doing design and coding work. |
| `illustration-outlined-cartoon` | Draws original hand-authored SVG spot illustrations in an outlined cartoon style for design and coding subjects. |
| `illustration-teal-spot` | Draws original spot illustrations of one hero object as SVG cards (480x360) in a teal-on-white style. |
| `illustration-two-colour-brush` | Draws original design and coding scenes as hand-authored SVG cards (480x360) in a two-colour brush-marker style. |
| `illustration-vintage-emblem` | Draws original hand-authored SVG badge illustrations in a vintage emblem style for design and coding subjects. |
| `image-first-grid-layout` | Create an image-led grid design system with full-bleed photography, structural guide lines, anchored content blocks, and restrained technical… |
| `implement-fog-of-war` | Implement, tune, debug, or validate soft wall-aware fog of war and gameplay perception in Three.js action games. |
| `interactive-topography` | Create thin elevation contours for a historical map and a raised relief view with interactive years, localized hover highlights and a… |
| `iterate-until-verified` | Apply a prompt-agnostic execution and verification loop to any substantial task while preserving the original request. |
| `landing-page` | Use when designing or rewriting a high-converting landing page (single-offer page) for SaaS/apps/services. |
| `landing-page-to-tutorial` | Run the whole chain for a long YouTube tutorial (15 to 25 minutes) that starts by designing and building landing pages with a coding model and ends… |
| `light-a-threejs-workspace` | Construct a procedural Three.js desk interior with textured furniture, a window and blinds, shadowed volumetric daylight, and coupled lighting… |
| `light-mode-paper-technical` | Create a light-mode technical design system with warm paper surfaces, dark outer framing, subtle diagonal texture, precise bracketed geometry, and… |
| `lightning-energy-skill-vfx` | Build the effects of a close-combat energy skill as one visual language in Three.js. |
| `liquid-metal-border` | Add and tune animated liquid-metal WebGL borders with the React `metal-fx` package. |
| `long-video-to-short` | Turn a finished long video (a tutorial, a making-of, a first impression) into a 60-second 9:16 short for Instagram Reels, YouTube Shorts and TikTok,… |
| `making-of-film` | Make Meng To's 4–5 minute "how I made X" YouTube film from a finished project or a brief, as the Greymourn Castle tutorial was made (Nov 2026) and… |
| `marquee-loop` | Apply seamless infinite marquee loops using duplicated items. |
| `masked-reveal` | Create masked staggered word reveals on scroll with GSAP ScrollTrigger. |
| `matterjs` | Use when implementing 2D physics interactions with Matter.js, including Engine/World setup, Render/Runner configuration, adding bodies and… |
| `mesh-gradient-dark-blue-clean` | Create a futuristic, premium, clean dark-blue mesh-gradient design system across background rendering, hero shell, navigation, floating nodes,… |
| `model-threejs-control-icons` | Model and light detailed Three.js icons for small interface controls. |
| `moss-glass-controls` | Build Sylva-style dark glass action pills and woodland cards with an inset rim, pale icon well and a gradient that travels around the edge on hover. |
| `neoclassical-ledger-ui` | Design parchment editorial interfaces with neoclassical object paintings, ledger typography and printed rules. |
| `nested-container-clean-agency` | Create a clean agency design system built from nested containers, with an outer editorial shell, inset dark feature blocks, rounded premium cards,… |
| `nested-container-frames` | Create a container-in-container layout system using nested frames. |
| `no-ai-design-slop` | Prevent and remove generic AI-generated design defaults, incoherent visual choices, and established UI defects while creating, revising, or… |
| `number-details` | Add decorative 01, 02, 03 numeric detail markers. |
| `operational-enterprise-ai` | Create or redesign enterprise AI, automation, security, and operations product pages that explain system boundaries, approvals, auditability,… |
| `optimize-threejs-games` | Profile, diagnose, and improve Three.js or WebGL game performance without regressing gameplay. |
| `optimize-web-animations` | Profile, audit, and optimize frontend page performance with emphasis on animation work, memory-leak risks, long-session slowdowns, CSS animations,… |
| `orange-clean-paper-saas` | Create a clean paper-toned SaaS design system with warm neutrals, orange accent signals, rounded premium forms, and polished product illustration… |
| `painted-product-showcase` | Build interactive HTML product demos over expansive painted landscapes, with translucent neutral panels, sample data, and stateful charts, invoices… |
| `paper-cinder-transition` | Change between pages, chapters or scenes with a paper-burn transition, a ragged ember line that sweeps across the frame, chars the old page ahead of… |
| `perching-butterfly` | Animate a small 3D butterfly that banks in flight, approaches an actual plant surface, settles with hinged wings and takes off when disturbed. |
| `performance-profiling` | Guide performance profiling for Apple platform apps with Instruments, Xcode diagnostics, and MetricKit. |
| `pointer-trail-emitter` | Build a cursor trail whose spacing stays constant at any hand speed, by emitting motes per unit of distance travelled rather than on a timer, so a… |
| `pollen-pointer-trail` | Emit a sparse, distance-spaced trail of airborne pollen from the pointer over a woodland scene, with depth drift, short lives and bounded particles. |
| `pricing-page` | Use when designing or rewriting a high-converting SaaS pricing page (structure, plan design, copywriting, SEO/AEO, FAQs, layout patterns,… |
| `product-proof-saas` | Create or redesign SaaS and AI product landing pages where a real workflow, interface, or deterministic demo is the central proof. |
| `progressive-blur` | Create a layered CSS progressive blur (top or bottom) using multiple backdrop-filter masks for depth and softness. |
| `publish-project-to-github` | Package a finished local project into an intentional GitHub repository, create a strong README and visual preview, push it safely, configure a… |
| `refract-liquid-glass` | Build sharp, draggable liquid-glass panels that bend a live backdrop through a rounded glass lip. |
| `release-threeui-demo` | Release an interactive web project on ThreeUI with a direct HTML preview, a verified 4K60 MP4, three open-source technique skills, and… |
| `relight-painted-surfaces` | Add pointer-driven lighting to a 2D painting, sprite, or holographic card using separate depth, normal, and roughness maps. |
| `reveal-hover-effect` | Build cursor-following spotlight reveals that expose a second aligned image through a soft radial mask. |
| `room-short-9x16` | Make a 60-second 9:16 short from a finished long video, set in the creator's own 3D room. |
| `scroll-mesh-survey` | Scrub a narrow topology scan across a visible 3D object and its companion editorial figures. |
| `scroll-progress-timeline` | Turn any ordered process into a data-driven vertical or horizontal scroll story with a base line, progress fill, active step states, responsive… |
| `scroll-scrubbed-object-handoff` | Choreograph a reversible scroll handoff between layered illustrations, transforming a held object into multiple moving pieces that land in a second… |
| `scroll-scrubbed-visual-sequence` | Build reversible scroll-controlled visual transformations with a pinned or sticky stage, normalized progress, and video, image-sequence, canvas,… |
| `scroll-scrubbed-word-reveal` | Reveal marked-up text word by word as scroll progress advances, while preserving semantic inline links, emphasis, responsive line wrapping, and… |
| `scroll-world-storytelling` | Turn an article, case study, brand narrative, product journey, or long-form story into a cinematic scroll-driven landing page using one of three… |
| `segmented-field-menu` | Create an inset upper-right navigation dock with compact icon-and-label segments, a pale selected segment and a matching footer dock for an… |
| `shade-glass-button-press` | Add fingertip-local press deformation and a refractive release wave to a glass button. |
| `shaders-cursor-ripples` | Add cursor-following fluid WebGPU distortion over an existing image with the Shaders library's ImageTexture and CursorRipples components. |
| `ship-web-games` | Package, deploy, and verify a playable Three.js or web game. |
| `skeuomorphic-ui` | Create skeuomorphic web UI surfaces with layered gradients, stacked inner and outer shadows, reflective gradient borders, micro texture, and… |
| `solar-duotone-bold` | Use Iconify Solar Duotone Bold icon style. |
| `split-layout-technical` | Create a technical split-screen design system with dual panels, fine frame lines, mono metadata, quiet editorial typography, and premium inset… |
| `staggered-word-reveal` | Create subtle editorial word-by-word text reveal animations where each word fades and rises into place once it enters the viewport. |
| `stitched-full-page-capture` | Capture or repair reliable full-page screenshots for lazy-loaded, scroll-animated, Framer, WebGL/canvas, or reveal-heavy web pages. |
| `sylva-field-guide-layout` | Lay out a botanical editorial UI with continuous vertical rules, sparse diagonal guides, large lightweight typography and aligned chapter labels and… |
| `tailwindcss` | Use when designing/implementing UI with Tailwind CSS (layout, typography, responsive, theming, component patterns). |
| `tech-green-dark-mode-modern` | Create a modern dark-mode technical design system with matte-black surfaces, emerald signal accents, mono system labeling, framed dashboard cards,… |
| `technical-wireframe-info-layout` | Create a monochrome technical wireframe design system with exploded 3D structure, connector annotations, sparse information labels, and precise dark… |
| `test-playable-web-games` | Test a playable browser game end to end with deterministic fixtures and real browser evidence. |
| `thinking-orbs` | Add accessible animated AI loading and agent-status indicators with the React thinking-orbs library. |
| `threejs` | Use when building or debugging interactive 3D scenes on the web with Three.js (scene/camera/renderer, lights/materials, GLTF loading, controls,… |
| `threejs-landscape` | Build a live Three.js landscape that stays quiet behind a subject — a noise heightfield on a polar grid so resolution follows the lens, ground… |
| `threejs-towers` | Generate architecture procedurally in Three.js and film it assembling — a small geometry vocabulary that builds pagodas, castles, domes and spires… |
| `threejs-weather` | Put weather into a Three.js scene that reads as weather — rain anchored inside the frustum, a storm that is the rain leaned on rather than a second… |
| `tune-enemy-ai` | Build, debug, balance, or test combat enemy AI for playable action games. |
| `unicorn-studio` | Use when embedding and customizing Unicorn Studio interactive animations on the web (embed, responsive sizing, performance, layering with UI,… |
| `unsplash-asset-images` | Use when you need to pick high-quality Unsplash images for product/design assets (avatars, headshots, portraits, large website backgrounds, and… |
| `url-to-motion-design` | Turn a launch film, product video or post at a URL (an X or Twitter post, YouTube, Vimeo, a direct video link) into Fil HTML motion scenes. |
| `vantajs` | Use when adding animated WebGL background effects with Vanta.js (setup, parameters, resizing, performance, integration in React/Next.js). |
| `video-to-superprompt` | Turn a reference video into a super detailed recreation or inspiration prompt. |
| `water-crystal-skill-vfx` | Build the effects of a water and crystal skill as one visual language in Three.js. |
| `web-technique-to-skill` | Turn a visual or interaction technique you already built into a reusable web-design skill, by isolating the one mechanism that makes it work while… |
| `webgl-3d-object` | Create a real 3D WebGL object with geometric mesh depth, physically based material, directional and ambient lighting, perspective camera, subtle… |
| `webgl-landing-steering` | Use when creating or refining WebGL-heavy landing pages and you need to steer toward a specific visual outcome (premium, technical, playful,… |
| `webgl-laser` | Create a fixed full-screen WebGL laser background effect with a thin white-hot vertical core, restrained brand-colored halo, and soft smoky fog… |
| `woodland-chapter-cameras` | Stage a live Three.js valley with a creek, instanced trees and layered fog across a hero, story chapter and footer using distinct scroll-driven… |
| `workflow-progress-screenshots` | Show the user real screenshots of the work as it progresses, without being asked. |
| `workflow-score-to-target` | Score work out of 10 against a clear rubric, then improve it round by round until every item reaches the target score the user named (for example… |
| `workflow-ship-change` | Ship every change the way the user requires, with the guardrails. |
| `workflow-threads-manager` | Oversee the other Claude threads (sessions) working on the same project. |
| `write-like-meng-on-x` | Write, rewrite, review, or continuously refine X/Twitter posts in Meng To's current voice using his deduplicated authored-post corpus, personal and… |
| `x-bookmark-quote-posts` | Check a user's latest X/Twitter bookmarks and turn recent saved posts into source-backed quote-post drafts calibrated against the user's latest 100… |

</details>

<details>
<summary><b>website-dev-21st</b> · 8 skills · by 21st.dev</summary>

| Skill | What it does |
|---|---|
| `21st-ai` | Generate and iterate on UI with 21st AI from the terminal via the `21st` CLI (`@21st-dev/cli`): sketch a UI from a prompt, preview the variants in… |
| `21st-cli-use` | Search, install and pull code from the 21st.dev catalog with the `21st` CLI (`@21st-dev/cli`): find React/shadcn components, themes and templates,… |
| `21st-design-sync` | Look at the current project's design (its shadcn / Tailwind CSS variables and color tokens) and publish it to the 21st.dev community as a shareable… |
| `21st-registry` | Publish your own work to 21st.dev and manage it from the terminal with the `21st` CLI (`@21st-dev/cli`): publish a React component to a team… |
| `21st-ui` | Find, install, and generate UI with 21st.dev. |
| `21st-ui-build` | Build or substantially change production UI using the current project's design context, existing components, and grounded 21st inspiration. |
| `21st-ui-explore` | Explore and compare multiple meaningfully different UI directions grounded in the current project's design system and 21st inspiration. |
| `21st-ui-review` | Review existing UI against the project's design context, accessibility expectations, responsive behavior, interaction quality, and high-confidence… |

</details>


## Troubleshooting

| Problem | Fix |
|---|---|
| **Upload says plugin validation failed** | Download the file again from this repo. Every skill here passes the validator (`python3 scripts/build.py --check`). If you edited a skill, keep its description under 1024 characters and without `<` or `>`. |
| **Upload says plugin.json must be at the root** | Upload the `.plugin` file as it is. Don't unzip it and re-zip the parent folder. |
| **A skill never seems to run** | Describe the task more specifically, or call it directly with `/` (claude.ai) or `/plugin-name:skill-name` (Claude Code). Some skills only run by name. |
| **The plugin is installed but skills are missing** | Open **Customize > Plugins**, open the plugin and check that its toggle is on. In Claude Code run `/reload-plugins` or start a new session. |
| **Too many similar skills load** | Install only the plugins you need instead of the all-in-one bundle, or turn off plugins you aren't using. |
| **shadcn connector doesn't work on claude.ai web** | It runs a local command (`npx shadcn@latest mcp`), so it only works in Claude Code and the desktop app, with Node.js 18 or newer installed. |
| **21st.dev skills ask for a login** | Run `npx @21st-dev/cli login`, or create an API key at https://21st.dev/mcp and set `TWENTYFIRST_TOKEN`. |
| **`claude plugin install` says plugin not found** | Use the name exactly as listed, with `@aiwithrakshi` at the end, for example `website-dev-gsap@aiwithrakshi`. Run `claude plugin marketplace update aiwithrakshi` first. |
| **Script says Claude Code is not installed** | Install Claude Code from https://code.claude.com/docs, open a new terminal, then run the script again. |

## FAQ

**Is it free?** Yes. The skills are open source and so is this packaging. You need your own Claude account to use them.

**Who wrote the skills?** The original authors in the [credits](#credits-and-licenses). This repository collects them, fixes descriptions so they pass Claude's validator, renames the plugins consistently, and adds install files, docs and scripts. Each plugin's `NOTICE.md` lists exactly what changed.

**All-in-one or separate plugins?** The bundle is the quickest way to try everything. Separate plugins are better for daily use: fewer skills means Claude picks the right one more reliably, and you can turn groups on and off.

**Do 343 skills slow Claude down?** Claude only reads a skill's short description until a task needs it, then loads the full instructions. Still, if you see the wrong skill being picked, install fewer plugins.

**Can I use these at work or in client projects?** Yes, under each skill's license (almost all are MIT; the 21st.dev skills are Apache-2.0 and ISC). Keep the license files when you share them.

**How do I update?** Marketplace installs: **Check for updates** in Customize > Plugins, or `claude plugin marketplace update aiwithrakshi` in Claude Code. File uploads: download the new `.plugin` file and upload it again.

**Is this affiliated with Anthropic, GSAP, Vercel or the authors?** No. It's a community collection. Product names belong to their owners.

## Rebuild or contribute

```bash
pip install pyyaml
python3 scripts/build.py --check   # validate every skill, change nothing
python3 scripts/build.py           # rebuild plugin.json files, READMEs, docs, catalog.json and dist/*.plugin
claude plugin validate .           # optional: Claude Code's own marketplace check
```

Repository layout:

```text
.claude-plugin/marketplace.json   marketplace for Claude Code and Customize > Plugins > Add marketplace
plugins/<name>/                   one folder per plugin: skills/, LICENSE, NOTICE.md, README.md
dist/*.plugin                     ready-to-upload files, including the all-in-one bundle
docs/SKILLS.md                    every skill with its full description
catalog.json                      the same list as data (plugin, skill, how to call it)
scripts/plugins.json              plugin names, credits and sample prompts (edit this, then build)
scripts/build.py                  validator and builder
scripts/install-claude-code.*     install all plugins into Claude Code
```

To suggest a skill, report a broken one or ask for a change, open an issue or a pull request. If you are one of the original authors and want your work changed or removed, open an issue and it will be handled quickly.

## Credits and licenses

The packaging in this repository (scripts, manifests, marketplace file and documentation) is released under the [MIT License](LICENSE). **Each skill keeps its author's license**, included in every plugin folder and in the bundle's `licenses/` folder. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

| Plugin | Written by | Original repository | License |
|---|---|---|---|
| `website-dev-design-taste` | Leonxlnx | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | MIT |
| `website-dev-emil-motion` | Emil Kowalski | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| `website-dev-gsap` | GreenSock | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | MIT |
| `website-dev-framer-motion` | C-Jeril (kuakua-app) | [C-Jeril/framer-motion-skills](https://github.com/C-Jeril/framer-motion-skills) | MIT |
| `website-dev-motion-design` | LottieFiles | [lottiefiles/motion-design-skill](https://github.com/lottiefiles/motion-design-skill) | MIT |
| `website-dev-ui-polish` | Julien Thibeaut (ibelick) | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | MIT |
| `website-dev-interface-guidelines` | Vercel Labs | [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | MIT |
| `website-dev-ux-product` | Uxcel Lab | [Uxcel-Lab/product-skills](https://github.com/Uxcel-Lab/product-skills) | MIT |
| `website-dev-oil-ui` | oil-oil | [oil-oil/oil-ui](https://github.com/oil-oil/oil-ui) | MIT |
| `website-dev-stageshow` | Benji Taylor | [benjitaylor/skills](https://github.com/benjitaylor/skills) | MIT |
| `website-dev-dimensional-drawing` | Enes Ozturk | [enesozturk/dimensional-drawing](https://github.com/enesozturk/dimensional-drawing) | MIT |
| `website-dev-frontend-slides` | Zara Zhang | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | MIT |
| `website-dev-mengto-collection` | Meng To | [MengTo/Skills](https://github.com/MengTo/Skills) | MIT |
| `website-dev-21st` | 21st.dev | [21st-dev/skill](https://github.com/21st-dev/skill) + [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) | Apache-2.0 (21st-dev/skill) and ISC (21st-ui from 21st-dev/magic-mcp) |
| `website-dev-shadcn-mcp` | shadcn | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | Configuration only (MIT, this repository); the shadcn CLI itself is MIT |

Thank you to every author for publishing their work openly. Please star their repositories.

---

Made in Karnataka by **Rakshith** · Founder, MyDesignNexus · Instagram: [@AIwithRakshith (Kannada)](https://www.instagram.com/aiwithrakshi) · [@aiwithrakshi.global](https://www.instagram.com/aiwithrakshi.global) · [@mydesignnexus.in](https://www.instagram.com/mydesignnexus.in)
