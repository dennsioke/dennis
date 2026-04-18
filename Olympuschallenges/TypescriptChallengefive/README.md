Repository
https://github.com/rcaferati/react-awesome-slider
Commit: 09a811b8f4a62d90b52664ab2dd06727c83a3265

Title
Autoplay with per-slide duration and direction control

Implement autoplay directly in the core AwesomeSlider component (src/core/index.tsx), not in the existing HOC wrapper (src/hoc/autoplay/).
autoplay (boolean, default false) -- enables automatic slide advancement when set to true.
autoplayInterval (number, default 3000) -- milliseconds between slide transitions.
autoplayDirection ("next" | "prev", default "next") -- direction of automatic advancement.
autoplaySpeed (number, default 1) -- multiplier applied to the effective duration. The effective duration is computed as interval / speed (rounded to the nearest integer). A speed of 2 halves the dwell time; 0.5 doubles it. Invalid values (0, negative, NaN, Infinity) must fall back to 1.
pauseOnHover (boolean, default false) -- when true, a mouseenter on the slider wrapper pauses the autoplay timer and mouseleave resumes it. An imperative pause() must take precedence: if pause() was called, a subsequent mouseleave must not resume autoplay.
Individual media items can override the global interval by including a numeric duration property in milliseconds (e.g. { slug: 'intro', duration: 5000 }). Only strictly positive values (duration > 0) are accepted as per-slide overrides; zero, negative, and NaN fall back to autoplayInterval. Infinity is treated as a positive value but produces an effective duration of 50ms (the hard minimum) after clamping. The final effective duration (after speed scaling) is always clamped to a minimum of 50ms and rounded to the nearest integer.
Autoplay must be suppressed when the existing disabled prop is true, when there is only a single slide, or while the component has not yet started (e.g. startup is false with a startupScreen). When the existing infinite prop is false, autoplay must stop at the terminal slide rather than wrapping. The component's imperative ref (via React.forwardRef) must expose play() and pause() methods that resume and suspend autoplay without changing the current slide position. Calling play() while already playing must be idempotent -- it must not stack duplicate timers, even when called hundreds of times or rapidly interleaved with pause(). Any manual navigation, whether through arrow buttons or bullet clicks, must cancel the pending autoplay timer and reschedule it using the incoming slide's effective duration. Unmounting the component must dispose of all autoplay timers.
Do not alter the existing direction computation in src/core/index.tsx that determines the `direction` boolean when the `selected` prop changes.
