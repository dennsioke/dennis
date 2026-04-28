Repository
https://github.com/rcaferati/react-awesome-slider
Commit: 09a811b8f4a62d90b52664ab2dd06727c83a3265

Title
Autoplay with per-slide duration and direction control

Add autoplay directly to the core `AwesomeSlider` component — not a HOC or wrapper.

Props added to `AwesomeSlider`:

- `autoplay` — enables cycling (default `false`)
- `autoplayInterval` — dwell time in ms (default `3000`)
- `autoplayDirection` — `"next"` | `"prev"` (default `"next"`)
- `autoplaySpeed` — divides all dwell times; invalid values (0, negative, NaN, non-finite) fall back to 1
- `pauseOnHover` — pauses while the cursor is over the `.awssld__wrapper` element

Per-slide override: a `duration` key on a slide object replaces `autoplayInterval` for that slide. Only strictly positive finite values are accepted; zero, negative, and NaN fall back to `autoplayInterval`; `Infinity` is accepted but capped. Effective dwell is always `Math.max(50, Math.round(interval / speed))`.

Autoplay is suppressed when `disabled` is true, there is only one slide, or the startup screen is still active. With `infinite={false}` it stops at the terminal slide; `play()` at a terminal slide in non-infinite mode is a no-op.

Ref methods `play()` and `pause()` are added to `AwesomeSliderHandle`. A programmatic `pause()` takes precedence over hover-leave — mouse leaving the wrapper must not resume autoplay if `pause()` was called explicitly. Manual navigation (arrows or bullets) cancels the current timer and schedules a fresh one using the destination slide's effective dwell. Autoplay-triggered navigation fires `onTransitionStart` and `onTransitionEnd` identically to manual navigation. All timers are cleared on unmount.