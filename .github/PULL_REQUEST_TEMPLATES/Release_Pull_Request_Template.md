## Checklist for releases:

#### Before a release:
- [ ] Provide complete validation shapes for the new ontology terms; remove shapes for the old ones
- [ ] Update changelogs
- [ ] Rerun ontology creation script (`create-ontology-ttl.sh`) with the version number of the release. E.g., `create-ontology-ttl.sh 4.2.0`
- [ ] Update and validate the examples against the latest ontology version and SHACL shapes
- [ ] Make sure that the manually authored parts of the documentation are in sync with the rest of the implementation and documentation
- [ ] Check whether the [IDS-G-pre](https://github.com/International-Data-Spaces-Association/IDS-G-pre/tree/main/Infomodel) documentation is up to date
- [ ] Check whether the [IDS Information Model Readme.md](https://github.com/International-Data-Spaces-Association/InformationModel/#readme) is up to date

### After a release:
- [ ] Generate human-readable documentation and single-file serializations using Widoco
- [ ] Generate Java library
- [ ] Update the message table
