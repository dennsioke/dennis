Repository
https://github.com/rcaferati/react-awesome-slider
Commit: 09a811b8f4a62d90b52664ab2dd06727c83a3265

Title
Autoplay with per-slide duration and direction control

The slider has no built-in way to advance slides without user interaction. This adds autoplay as a first-class feature directly in `AwesomeSlider` -- not a HOC or wrapper -- so all props and ref methods are available on the base component.
`autoplay` -- enables cycling (default `false`)
`autoplayInterval` -- dwell time in ms (default `3000`)
`autoplayDirection` -- `"next"` | `"prev"` (default `"next"`)
`autoplaySpeed` -- scales dwell as `interval / speed` (default `1`); zero, negative, NaN, and non-finite values fall back to `1`
`pauseOnHover` -- pauses while the cursor is over the `.awssld__wrapper` element; `mouseenter` pauses, `mouseleave` resumes
A `duration` key on a slide object overrides `autoplayInterval` for that slide. Only strictly positive finite values are used; zero, negative, and NaN fall back to `autoplayInterval`. If `duration` is `Infinity`, treat the effective dwell as 50ms (the minimum). For all other valid values, effective dwell is `Math.max(50, Math.round(interval / speed))`.
Autoplay does not run when `disabled` is true, when there is only one slide, or while the startup screen is active. With `infinite={false}` it stops at the terminal slide; `play()` while already at the terminal is a no-op.
`play()` and `pause()` are added to `AwesomeSliderHandle`. Both are safe no-ops when autoplay is suppressed. `play()` is idempotent -- calling it while already running does not stack timers. A programmatic `pause()` takes precedence over hover-leave: `mouseleave` does not resume autoplay if `pause()` was called explicitly. Likewise, `onTransitionEnd` does not reschedule autoplay while the cursor is still over the wrapper.
Any navigation -- arrows, bullets, or a same-slide no-op -- cancels the current timer and schedules a fresh one using the destination slide's effective dwell. Autoplay-triggered navigation fires `onTransitionStart` and `onTransitionEnd` identically to manual navigation. All timers are cleared on unmount.