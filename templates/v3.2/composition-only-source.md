# Composition-only source policy

When the user supplies an image to follow its composition but does not request reference-image generation:

1. Inspect the source and extract only spatial/compositional facts: aspect/orientation, camera height/angle, subject placement, subject scale, negative space, action vector, foreground/background layering, major prop placement, depth-of-field pattern, horizon/background bands.
2. Record them as COMPOSITION LOCKS.
3. Do not attach the source image to the generator.
4. Do not copy identity, face, wardrobe, logos, brands, venue-specific marks, textures, artifacts, or AI signatures unless explicitly requested.
5. Compile a fresh scene from the composition locks and the current brief.
6. Current-task locks override any prior-task context.
