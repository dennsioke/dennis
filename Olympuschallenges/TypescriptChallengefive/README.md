Repository
https://github.com/rcaferati/react-awesome-slider
Commit: 09a811b8f4a62d90b52664ab2dd06727c83a3265

Title
Autoplay with per-slide duration and direction control

The react-awesome-slider library is widely used to build image carousels and content sliders in React applications. Currently, users must navigate through slides manually. We need the slider to support automatic playback so that content can advance on its own — a common requirement for hero banners, promotional carousels, and image galleries where continuous, hands-free progression improves the user experience.
Users should be able to enable autoplay and control how long each slide is displayed before the slider moves on. They should also be able to choose the direction of progression (forward or backward) and tune the overall playback speed independently of the base interval. For content-heavy slides that need more time, individual slides should be able to declare their own display duration rather than inheriting the global setting.
Autoplay should pause when a user hovers over the slider so they can read or interact with content at their own pace, then resume when they move away — unless they have explicitly paused playback themselves, in which case the hover-out should not restart it. The slider should also expose programmatic play and pause controls for cases where the host application needs to manage playback externally.
The feature should behave gracefully in edge cases: autoplay should not activate when the slider is disabled, when only one slide is present, or before the slider has finished initialising. When the slider is not configured to loop, autoplay should stop naturally at the last slide. Manual navigation via arrows or indicator bullets should seamlessly reset and reschedule the autoplay timer relative to the newly selected slide. All autoplay activity should be fully cleaned up when the component is removed from the page.