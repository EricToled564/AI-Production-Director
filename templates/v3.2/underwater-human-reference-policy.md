# Underwater Human Reference Policy v3.2

Use for complex underwater/split-level human images.

## Preserve first
- User/project locks remain verbatim across revisions.
- If the user gave a recognized domain pose/technique, preserve the domain label; do not expand it into speculative anatomy by default.

## Reference roles
Each reference has one role and explicit ignored dimensions. Example:
`REF1 = water physics only; ignore identity, pose, framing, camera, environment, color.`
Do not borrow an ignored dimension even when the source image makes it salient.

## Prompt revision
When the existing result is strong, use small deltas. Do not rewrite water, lighting, environment, subject, or pose when they already pass.

## Complex underwater anatomy
If fine upper-body anatomy is non-critical, physically plausible turbulence/bubbles may hide detail while preserving the required pose silhouette, frontal orientation, continuous proportions and body geometry.

## Crowd/background
Do not infer density. `audience present` does not imply `packed stands`. If the user later locks `stands full`, update only that background property.

## Camera geometry
Objects behind the camera under the locked viewpoint must not be visible. Treat camera-relative object visibility as a critical spatial invariant.

## Delivery
Aspect ratio belongs in generator settings when supported and must be checked on output pixels. Prompt text alone is not a delivery guarantee.
