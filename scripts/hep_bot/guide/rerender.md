# Render a feedstock
`@hep-bot rerender` brings a feedstock's CI and bot files up to date.

Every feedstock carries a few files copied from hep-forge/.github:
`.github/workflows/autoupload.yml` (the build), `.github/workflows/hep-bot-comment.yml`
(this bot), `README.md` and `AGENTS.md`. hep-bot refreshes them daily in every
feedstock registered in hep-forge/.github.

```
@hep-bot rerender                    in an issue of the feedstock
@hep-bot rerender <pkg>              anywhere
```

or the *Rerender feedstock* issue form. It registers the feedstock if it isn't yet and
renders it straight away. Your `recipe/` is not touched and nothing is published.

You need it when:

- the feedstock was created by hand (it isn't registered, so it never gets the files);
- a build fails because the workflow is old;
- you edited one of the rendered files by mistake.

Don't edit the rendered files in a feedstock: change the template in
[hep-forge/.github](https://github.com/hep-forge/.github/tree/main/scripts/templates),
which updates every feedstock.
