Repository
https://github.com/rcaferati/react-awesome-slider
Commit: 09a811b8f4a62d90b52664ab2dd06727c83a3265

Title
Autoplay with per-slide duration and direction control

A slider component should advance slides automatically, pause on hover, and respect per-slide timings. The following props govern the behavior:
`autoplay` (boolean, default false) -- enables automatic advancement.
`autoplayInterval` (number, default 3000) -- milliseconds between transitions.
`autoplayDirection` ('next' | 'prev', default 'next') -- direction of advancement.
`autoplaySpeed` (number, default 1) -- multiplier applied to the interval; invalid values (<= 0, NaN, Infinity) fall back to 1. A speed of 2 halves dwell time; 0.5 doubles it.
`pauseOnHover` (boolean, default false) -- when true, mouseenter on the `.awssld__wrapper` element pauses the timer and mouseleave resumes it (unless `pause()` was called imperatively, which takes permanent precedence over hover).
`infinite` (boolean) -- when false, autoplay stops at the terminal slide instead of wrapping.
`disabled` (boolean) -- suppresses autoplay entirely.
`startupScreen` / `startup` -- while `startup` is false, the startupScreen replaces the main slider UI (bullets, slides, etc. are not rendered); autoplay only begins once the startup sequence completes.
Per-slide duration overrides: a media item may carry a numeric `duration` (ms). Only values > 0 are accepted; duration <= 0 or NaN falls back to `autoplayInterval`. `duration: Infinity` is coerced to 50 ms (i.e., treated as immediate and clamped to the hard minimum). All effective durations are clamped to a minimum of 50 ms and rounded to the nearest integer after speed scaling.
Manual navigation (arrows or bullets) cancels the pending timer and reschedules it using the incoming slide's effective duration. `play()` / `pause()` are exposed imperatively; calling `play()` while already playing is a no-op -- no stacked timers. All timers are disposed on unmount.
`onTransitionStart` (callback) -- fired when a slide transition begins (whether triggered by autoplay or manual navigation).
`onTransitionEnd` (callback) -- fired when a slide transition completes.