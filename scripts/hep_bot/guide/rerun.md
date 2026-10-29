# Rebuild a tag
`@hep-bot rerun` rebuilds and re-publishes an existing tag.

```
@hep-bot rerun <tag>                 in an issue of the feedstock
@hep-bot rerun <pkg> <tag>           in an issue of hep-forge/.github
```

Use it when a build failed for a reason outside the recipe: a runner hiccup, a
dependency that wasn't on the channel yet, an upstream download that was down. Both
architectures rebuild together, and hep-bot replies with a link to the run.

It builds the recipe **as it was at that tag**. To ship a recipe fix, merge it and move
the tag instead (`@hep-bot help release`). A tag that doesn't exist yet doesn't need
`rerun`: pushing it starts the build.

To rebuild a package together with everything that depends on it, in dependency order,
run the [ordered rebuild](https://github.com/hep-forge/.github/actions/workflows/hep-bot-rebuild.yml)
workflow.
