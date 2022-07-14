## Type of change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Formatting / Refactoring / Other change (non-breaking, non-functional changes)
- [ ] Release

## Checklist:
- [ ] Provide complete validation shapes for the new ontology terms; remove shapes for the old ones

### Checklist for releases:

#### Before a release:
- [ ] Ensure that the respective [GitHub milestone](https://github.com/International-Data-Spaces-Association/InformationModel/milestones) has no more open issues (i.e., close these or move these to subsequent milestones)
- [ ] Update changelogs
- [ ] Rerun ontology creation script (`create-ontology-ttl.sh`) with the version number of the release. E.g., `create-ontology-ttl.sh 4.2.0`
- [ ] Update and validate the examples against the latest ontology version and SHACL shapes
- [ ] Make sure that the manually authored parts of the documentation are in sync with the rest of the implementation and documentation
- [ ] Check whether the [IDS-G-pre](https://github.com/International-Data-Spaces-Association/IDS-G-pre/tree/main/Infomodel) documentation is up-to-date
- [ ] Check whether the [IDS Information Model Readme.md](https://github.com/International-Data-Spaces-Association/InformationModel/#readme) is up-to-date

### After a release:
- [ ] Generate human-readable documentation and single-file serializations using Widoco
- [ ] Generate Java library
- [ ] Update the message table
