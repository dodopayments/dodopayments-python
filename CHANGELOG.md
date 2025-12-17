# Changelog

## 1.67.1 (2025-12-17)

Full Changelog: [v1.67.0...v1.67.1](https://github.com/dodopayments/dodopayments-python/compare/v1.67.0...v1.67.1)

### Chores

* speedup initial import ([7d9c41f](https://github.com/dodopayments/dodopayments-python/commit/7d9c41fa12b6b8d3358b6f8707b2904f85ac9f2b))

## 1.67.0 (2025-12-16)

Full Changelog: [v1.66.2...v1.67.0](https://github.com/dodopayments/dodopayments-python/compare/v1.66.2...v1.67.0)

### Features

* **api:** updated openapi spec to 1.67.0 ([f5b9e26](https://github.com/dodopayments/dodopayments-python/commit/f5b9e26e4d8aece37f00c37e53d8242696a3e599))


### Chores

* **internal:** add missing files argument to base client ([3b53953](https://github.com/dodopayments/dodopayments-python/commit/3b539538c96ad8e72573efaf152a69071e821007))

## 1.66.2 (2025-12-12)

Full Changelog: [v1.66.1...v1.66.2](https://github.com/dodopayments/dodopayments-python/compare/v1.66.1...v1.66.2)

### Features

* **api:** manual updates ([5525a18](https://github.com/dodopayments/dodopayments-python/commit/5525a18d9fa48c4ee0cf8f7d4075cdfbcbdf4ee8))

## 1.66.1 (2025-12-09)

Full Changelog: [v1.66.0...v1.66.1](https://github.com/dodopayments/dodopayments-python/compare/v1.66.0...v1.66.1)

### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([b72a3db](https://github.com/dodopayments/dodopayments-python/commit/b72a3db8c753bc71f037290268a0ade1b77b09fe))


### Chores

* add missing docstrings ([d90b3ba](https://github.com/dodopayments/dodopayments-python/commit/d90b3bacdfa6f399ac6f678c786a4280f8660241))

## 1.66.0 (2025-12-08)

Full Changelog: [v1.61.7...v1.66.0](https://github.com/dodopayments/dodopayments-python/compare/v1.61.7...v1.66.0)

### Features

* **api:** updated openapi spec to v1.66.1 ([178d890](https://github.com/dodopayments/dodopayments-python/commit/178d89003f56d20d5edd0ab8c7cccaed18fcdddc))

## 1.61.7 (2025-12-03)

Full Changelog: [v1.61.6...v1.61.7](https://github.com/dodopayments/dodopayments-python/compare/v1.61.6...v1.61.7)

### Chores

* **docs:** use environment variables for authentication in code snippets ([b7a6103](https://github.com/dodopayments/dodopayments-python/commit/b7a61030974a56a5afabb2f4cec4f1921dfc53f9))
* update lockfile ([e58ee31](https://github.com/dodopayments/dodopayments-python/commit/e58ee315dba2c08c21b5e820f1210d7a19206b00))

## 1.61.6 (2025-11-28)

Full Changelog: [v1.61.5...v1.61.6](https://github.com/dodopayments/dodopayments-python/compare/v1.61.5...v1.61.6)

### Bug Fixes

* ensure streams are always closed ([404bff6](https://github.com/dodopayments/dodopayments-python/commit/404bff687fee8ac9d399aafebceb36375b37ac62))


### Chores

* add Python 3.14 classifier and testing ([b06ff6b](https://github.com/dodopayments/dodopayments-python/commit/b06ff6bae8bdad8f501a215127f3c361bea33e70))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([4bfb430](https://github.com/dodopayments/dodopayments-python/commit/4bfb430e41637e1385e04d18d323ba4dda55b106))

## 1.61.5 (2025-11-17)

Full Changelog: [v1.60.0...v1.61.5](https://github.com/dodopayments/dodopayments-python/compare/v1.60.0...v1.61.5)

### Features

* **api:** updated openapi spec to v1.61.5 ([4e9b3e9](https://github.com/dodopayments/dodopayments-python/commit/4e9b3e91695cc5f6ca1a75ac39e58d7aee15d78e))


### Chores

* **internal:** codegen related update ([fa08219](https://github.com/dodopayments/dodopayments-python/commit/fa08219038a929ab1cb48f92a3f806db08e22e91))

## 1.60.0 (2025-11-14)

Full Changelog: [v1.56.7...v1.60.0](https://github.com/dodopayments/dodopayments-python/compare/v1.56.7...v1.60.0)

### Features

* **api:** added update payment method and updated openapi spec to v1.60.0 ([6041189](https://github.com/dodopayments/dodopayments-python/commit/60411890199ee74490dd244e49e9727e8028f27d))

## 1.56.7 (2025-11-12)

Full Changelog: [v1.56.6...v1.56.7](https://github.com/dodopayments/dodopayments-python/compare/v1.56.6...v1.56.7)

### Bug Fixes

* compat with Python 3.14 ([8aa3fe5](https://github.com/dodopayments/dodopayments-python/commit/8aa3fe57d419077ca43fec02092a3cf92b88c3b0))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([763bb2b](https://github.com/dodopayments/dodopayments-python/commit/763bb2b25b61308e99e783c8e8fb9adf61cbabe6))


### Chores

* **package:** drop Python 3.8 support ([d7d9c93](https://github.com/dodopayments/dodopayments-python/commit/d7d9c93751304ab0117ba69564372a2e1f95055b))

## 1.56.6 (2025-11-08)

Full Changelog: [v1.56.5...v1.56.6](https://github.com/dodopayments/dodopayments-python/compare/v1.56.5...v1.56.6)

### Chores

* **internal:** codegen related update ([380a413](https://github.com/dodopayments/dodopayments-python/commit/380a4136a377e5f94896381a1d0e8e7a112ebd63))

## 1.56.5 (2025-11-07)

Full Changelog: [v1.56.4...v1.56.5](https://github.com/dodopayments/dodopayments-python/compare/v1.56.4...v1.56.5)

### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([780f7c2](https://github.com/dodopayments/dodopayments-python/commit/780f7c2389bc973b355130d2860c734dd569cf71))
* **internal:** codegen related update ([c27693d](https://github.com/dodopayments/dodopayments-python/commit/c27693dd7f198bb81bb1e0c43e315c91558d4554))
* **internal:** codegen related update ([edc21df](https://github.com/dodopayments/dodopayments-python/commit/edc21df89d16d1f72f3a6a82acd4b06e7c8d4d3e))
* **internal:** fix test definition ([d0e580e](https://github.com/dodopayments/dodopayments-python/commit/d0e580eea73ba5312de55c792d0318a8ad1143e1))
* **internal:** grammar fix (it's -&gt; its) ([519ecfa](https://github.com/dodopayments/dodopayments-python/commit/519ecfa053027914fd2f796631a75fca8e0336bd))

## 1.56.4 (2025-10-30)

Full Changelog: [v1.56.3...v1.56.4](https://github.com/dodopayments/dodopayments-python/compare/v1.56.3...v1.56.4)

### Bug Fixes

* **client:** close streams without requiring full consumption ([2f5eedd](https://github.com/dodopayments/dodopayments-python/commit/2f5eedda5739ad357d0a61579fb306140c468ad0))

## 1.56.3 (2025-10-29)

Full Changelog: [v1.56.2...v1.56.3](https://github.com/dodopayments/dodopayments-python/compare/v1.56.2...v1.56.3)

### Features

* **api:** updated openapi spec to v1.56.3 ([b0e5768](https://github.com/dodopayments/dodopayments-python/commit/b0e576841bb7d01e43521bf4d62d518267ce140f))

## 1.56.2 (2025-10-27)

Full Changelog: [v1.56.0...v1.56.2](https://github.com/dodopayments/dodopayments-python/compare/v1.56.0...v1.56.2)

### Features

* **api:** updated to openapi spec v1.56.0 ([f142f07](https://github.com/dodopayments/dodopayments-python/commit/f142f078dd7740c4538c8b267ff0f548d7de745e))

## 1.56.0 (2025-10-25)

Full Changelog: [v1.55.7...v1.56.0](https://github.com/dodopayments/dodopayments-python/compare/v1.55.7...v1.56.0)

### Features

* **api:** added unwrap functions for webhooks ([9bf339a](https://github.com/dodopayments/dodopayments-python/commit/9bf339a52c8660f603de53d68be20304e46cae57))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([e4792b3](https://github.com/dodopayments/dodopayments-python/commit/e4792b35b4bcf7365c815f3543eac7a5bda724ad))

## 1.55.7 (2025-10-17)

Full Changelog: [v1.55.0...v1.55.7](https://github.com/dodopayments/dodopayments-python/compare/v1.55.0...v1.55.7)

### Features

* **api:** updates for openapi spec v1.55.7 ([852a16f](https://github.com/dodopayments/dodopayments-python/commit/852a16ff188fe1ac4e7f4f555333844ad9f8157c))

## 1.55.0 (2025-10-16)

Full Changelog: [v1.53.5...v1.55.0](https://github.com/dodopayments/dodopayments-python/compare/v1.53.5...v1.55.0)

### Features

* **api:** updated openapi spec to v1.55.0 ([28c4ab1](https://github.com/dodopayments/dodopayments-python/commit/28c4ab1f8e76410575e3646c425d36cd3fae3abc))


### Chores

* **internal:** detect missing future annotations with ruff ([70df264](https://github.com/dodopayments/dodopayments-python/commit/70df2646b6fa82309691fdd974d44f0968fc2e80))

## 1.53.5 (2025-09-23)

Full Changelog: [v1.53.4...v1.53.5](https://github.com/dodopayments/dodopayments-python/compare/v1.53.4...v1.53.5)

### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([fd89d01](https://github.com/dodopayments/dodopayments-python/commit/fd89d01ee0e65b99a08cf1a139c587c83ef8588e))
* improve example values ([cab2f1e](https://github.com/dodopayments/dodopayments-python/commit/cab2f1e01ad09a478834024e3c5f83fef2cf7ab2))
* **types:** change optional parameter type from NotGiven to Omit ([cf2bf2d](https://github.com/dodopayments/dodopayments-python/commit/cf2bf2dc9c94a859186765cc87c8fdb0017286ce))

## 1.53.4 (2025-09-17)

Full Changelog: [v1.53.3...v1.53.4](https://github.com/dodopayments/dodopayments-python/compare/v1.53.3...v1.53.4)

### Chores

* **internal:** update pydantic dependency ([459d36f](https://github.com/dodopayments/dodopayments-python/commit/459d36f9ddf754b3f921e7e6e5b846ec6d353766))

## 1.53.3 (2025-09-13)

Full Changelog: [v1.53.2...v1.53.3](https://github.com/dodopayments/dodopayments-python/compare/v1.53.2...v1.53.3)

### Features

* **api:** added typescript sdk for migration and updated org info ([ea25f2f](https://github.com/dodopayments/dodopayments-python/commit/ea25f2f326df4000d1e85051398a9e1c2b49cd73))
* **api:** manual updates ([9db9f66](https://github.com/dodopayments/dodopayments-python/commit/9db9f66ae13049550c852d33a43eacfaf867fed4))

## 1.53.2 (2025-09-13)

Full Changelog: [v1.52.6...v1.53.2](https://github.com/dodopayments/dodopayments-python/compare/v1.52.6...v1.53.2)

### Features

* **api:** updated openapi spec to v1.53.2 with customer credits. ([92216ca](https://github.com/dodopayments/dodopayments-python/commit/92216ca3284a2f901e2977e2cc47ea9489da8d85))

## 1.52.6 (2025-09-06)

Full Changelog: [v1.52.5...v1.52.6](https://github.com/dodopayments/dodopayments-python/compare/v1.52.5...v1.52.6)

### Chores

* **internal:** move mypy configurations to `pyproject.toml` file ([1f2346b](https://github.com/dodopayments/dodopayments-python/commit/1f2346bbe5752fd8454d51cb54f0b2ae5e3f265b))
* **tests:** simplify `get_platform` test ([784f7d6](https://github.com/dodopayments/dodopayments-python/commit/784f7d6ac46d9d84db4fe0efe9ca739df6c082f0))

## 1.52.5 (2025-09-04)

Full Changelog: [v1.52.4...v1.52.5](https://github.com/dodopayments/dodopayments-python/compare/v1.52.4...v1.52.5)

### Features

* improve future compat with pydantic v3 ([e1d25a8](https://github.com/dodopayments/dodopayments-python/commit/e1d25a86243b79ca7a13b4e54548edcda0cff23a))

## 1.52.4 (2025-09-03)

Full Changelog: [v1.51.1...v1.52.4](https://github.com/dodopayments/dodopayments-python/compare/v1.51.1...v1.52.4)

### Features

* **api:** manual updates ([c7a7380](https://github.com/dodopayments/dodopayments-python/commit/c7a7380d715423f969d5cff24862ec38258d42f2))
* **api:** updated openapi spec ([dfc4ad4](https://github.com/dodopayments/dodopayments-python/commit/dfc4ad4c1920f57f9fe4e7629caaa1eab72913bf))
* **api:** updated openapi spec to v1.52.4 ([e0ca092](https://github.com/dodopayments/dodopayments-python/commit/e0ca0926d8093b5e65b24ed7a0306872d372ea0a))
* **types:** replace List[str] with SequenceNotStr in params ([42cf186](https://github.com/dodopayments/dodopayments-python/commit/42cf186779ff891c84db5bd1b8e888870d358697))
* updated openapi spec and added model and API functions for Usage Based Billing ([3c62736](https://github.com/dodopayments/dodopayments-python/commit/3c6273618b0c453aaa82df3aa97dbb3e2ae06ca4))

## 1.51.1 (2025-08-30)

Full Changelog: [v1.51.0...v1.51.1](https://github.com/dodopayments/dodopayments-python/compare/v1.51.0...v1.51.1)

### Bug Fixes

* avoid newer type syntax ([9480de5](https://github.com/dodopayments/dodopayments-python/commit/9480de5e0192ec77a8536457c3628a0ad386721d))


### Chores

* **internal:** add Sequence related utils ([aa4240b](https://github.com/dodopayments/dodopayments-python/commit/aa4240b143433f2f1964440595fa0be5fb14de7c))
* **internal:** change ci workflow machines ([2dd4020](https://github.com/dodopayments/dodopayments-python/commit/2dd4020d357b4ed6cb6d992340b6869186046282))
* **internal:** update pyright exclude list ([f6024a4](https://github.com/dodopayments/dodopayments-python/commit/f6024a4956e635c49679d3fa19b4a383e1aec444))

## 1.51.0 (2025-08-22)

Full Changelog: [v1.49.0...v1.51.0](https://github.com/dodopayments/dodopayments-python/compare/v1.49.0...v1.51.0)

### Features

* **api:** updated example ([d066c34](https://github.com/dodopayments/dodopayments-python/commit/d066c34600592052a4688ff37b14de7f7002c3c9))
* **api:** updated openapi spec to v1.51.0 and added checkout sessions ([79855e9](https://github.com/dodopayments/dodopayments-python/commit/79855e96b3157175ba2cfa3662f67b61bc68c160))


### Chores

* update github action ([660f3d7](https://github.com/dodopayments/dodopayments-python/commit/660f3d7f30460bf3b971f33981b42fff3c4a636e))

## 1.49.0 (2025-08-13)

Full Changelog: [v1.47.0...v1.49.0](https://github.com/dodopayments/dodopayments-python/compare/v1.47.0...v1.49.0)

### Features

* **api:** manual updates ([a81ec37](https://github.com/dodopayments/dodopayments-python/commit/a81ec3716e6ee39d5b8e362583ef6f21cc8538fe))
* **api:** manual updates ([5480a5d](https://github.com/dodopayments/dodopayments-python/commit/5480a5dfa9743308834c1c8191e36c76dc616fc1))
* **api:** updated code for v1.49.0 ([72d4d8a](https://github.com/dodopayments/dodopayments-python/commit/72d4d8abadedba6421a23245c9e60612e80db13b))

## 1.47.0 (2025-08-11)

Full Changelog: [v1.44.0...v1.47.0](https://github.com/dodopayments/dodopayments-python/compare/v1.44.0...v1.47.0)

### Features

* **api:** updated openapi spec to 1.47.0 ([afc16dd](https://github.com/dodopayments/dodopayments-python/commit/afc16dd0b858b3a7e91287156733fa6b7c4e4572))


### Chores

* **internal:** fix ruff target version ([0f496bc](https://github.com/dodopayments/dodopayments-python/commit/0f496bcc9fb01e3ed5568b58d536fefd1e333df7))
* **internal:** update comment in script ([d40fb67](https://github.com/dodopayments/dodopayments-python/commit/d40fb67d7fa0bea2455969835debcbbb8aa2ab73))
* update @stainless-api/prism-cli to v5.15.0 ([772b0ca](https://github.com/dodopayments/dodopayments-python/commit/772b0cae7a82a93f2d8e6f45b83ebca6941bd93d))

## 1.44.0 (2025-08-02)

Full Changelog: [v1.43.1...v1.44.0](https://github.com/dodopayments/dodopayments-python/compare/v1.43.1...v1.44.0)

### Features

* **api:** updated openapi spec to 1.44.0 ([fad1533](https://github.com/dodopayments/dodopayments-python/commit/fad1533668d7cf2d3bda6b0d40a01f85c244723f))
* **client:** support file upload requests ([4ebfcb1](https://github.com/dodopayments/dodopayments-python/commit/4ebfcb160f5ecb4c8f86e46d5767395344614165))

## 1.43.1 (2025-07-25)

Full Changelog: [v1.43.0...v1.43.1](https://github.com/dodopayments/dodopayments-python/compare/v1.43.0...v1.43.1)

### Chores

* **project:** add settings file for vscode ([dcc13b8](https://github.com/dodopayments/dodopayments-python/commit/dcc13b814a78d0147d9d621aca865edd779a8b31))

## 1.43.0 (2025-07-23)

Full Changelog: [v1.42.0...v1.43.0](https://github.com/dodopayments/dodopayments-python/compare/v1.42.0...v1.43.0)

### Features

* **api:** updated openapi spec to v1.42.5 ([08a0bf9](https://github.com/dodopayments/dodopayments-python/commit/08a0bf9aa2adc4ef10644655ae61c73fcdb4a505))


### Bug Fixes

* **parsing:** ignore empty metadata ([20c799d](https://github.com/dodopayments/dodopayments-python/commit/20c799ddc02003fc43661fbaf29924b473fc1fde))
* **parsing:** parse extra field types ([d00f70a](https://github.com/dodopayments/dodopayments-python/commit/d00f70a16e83d3994d1c8f4d7d0cac9b0cfcd1e3))

## 1.42.0 (2025-07-16)

Full Changelog: [v1.39.0...v1.42.0](https://github.com/dodopayments/dodopayments-python/compare/v1.39.0...v1.42.0)

### Features

* **api:** updated open api spec to v1.42.0 ([ea2b952](https://github.com/dodopayments/dodopayments-python/commit/ea2b952352ee4470f4dbace6969f91511331a166))

## 1.39.0 (2025-07-15)

Full Changelog: [v1.38.2...v1.39.0](https://github.com/dodopayments/dodopayments-python/compare/v1.38.2...v1.39.0)

### Features

* **api:** updated openapi spec to v1.40.0 ([91da77a](https://github.com/dodopayments/dodopayments-python/commit/91da77acd02f39295613e55454005f0a90bca600))
* clean up environment call outs ([8bbe9b4](https://github.com/dodopayments/dodopayments-python/commit/8bbe9b4cccc55a6f08fd9760b45aa46b94bc6a2d))

## 1.38.2 (2025-07-12)

Full Changelog: [v1.38.1...v1.38.2](https://github.com/dodopayments/dodopayments-python/compare/v1.38.1...v1.38.2)

### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([9807cc2](https://github.com/dodopayments/dodopayments-python/commit/9807cc2f47241f9168c7eb766c7c9f0e8f32e4ad))
* **parsing:** correctly handle nested discriminated unions ([4147e1f](https://github.com/dodopayments/dodopayments-python/commit/4147e1ffcf8c2790e21c9667ce759086612e4e1e))


### Chores

* **readme:** fix version rendering on pypi ([5f7a3c2](https://github.com/dodopayments/dodopayments-python/commit/5f7a3c2c710878faaa7840a9d82eb3cab5f761c5))

## 1.38.1 (2025-07-09)

Full Changelog: [v1.38.0...v1.38.1](https://github.com/dodopayments/dodopayments-python/compare/v1.38.0...v1.38.1)

### Chores

* **internal:** bump pinned h11 dep ([15fb329](https://github.com/dodopayments/dodopayments-python/commit/15fb329df9bb33ff404749c52a669ba2186f8774))
* **package:** mark python 3.13 as supported ([4b11468](https://github.com/dodopayments/dodopayments-python/commit/4b11468685b9d7c6a7ad157f51de41c89469ae81))

## 1.38.0 (2025-07-05)

Full Changelog: [v1.37.1...v1.38.0](https://github.com/dodopayments/dodopayments-python/compare/v1.37.1...v1.38.0)

### Features

* **api:** updated openapi spec to v1.38.0 ([3709f27](https://github.com/dodopayments/dodopayments-python/commit/3709f27acaaf362e6ce7009abfd3a5f0390b71eb))

## 1.37.1 (2025-07-03)

Full Changelog: [v1.37.0...v1.37.1](https://github.com/dodopayments/dodopayments-python/compare/v1.37.0...v1.37.1)

### Features

* **api:** added webhook event type model ([5ce6fd3](https://github.com/dodopayments/dodopayments-python/commit/5ce6fd3edbbfbe36def6a1dd3b784af83527993d))
* **api:** added webhook payload model ([1f231a1](https://github.com/dodopayments/dodopayments-python/commit/1f231a10af884c552cace741f9fc2623d7df8f84))

## 1.37.0 (2025-07-02)

Full Changelog: [v1.34.3...v1.37.0](https://github.com/dodopayments/dodopayments-python/compare/v1.34.3...v1.37.0)

### Features

* **api:** updated openapi spec for v1.37.0 ([9e301cf](https://github.com/dodopayments/dodopayments-python/commit/9e301cfffd01bfcef66fe6a97b733ba7b7996c8d))

## 1.34.3 (2025-07-02)

Full Changelog: [v1.34.2...v1.34.3](https://github.com/dodopayments/dodopayments-python/compare/v1.34.2...v1.34.3)

### Bug Fixes

* **ci:** correct conditional ([09abb22](https://github.com/dodopayments/dodopayments-python/commit/09abb22939f29c6d3b96ecd5a64bb0facc40db90))
* **ci:** release-doctor — report correct token name ([84b7ffc](https://github.com/dodopayments/dodopayments-python/commit/84b7ffca299ebd7888f63d34ac32130c68c2b448))


### Chores

* **ci:** change upload type ([ebc5951](https://github.com/dodopayments/dodopayments-python/commit/ebc59514858e3782bd07305b8b16a1365bbd346d))
* **ci:** only run for pushes and fork pull requests ([0e6b873](https://github.com/dodopayments/dodopayments-python/commit/0e6b873a9d03b3860f2402a04cfe72b6c54d3fef))

## 1.34.2 (2025-06-24)

Full Changelog: [v1.34.1...v1.34.2](https://github.com/dodopayments/dodopayments-python/compare/v1.34.1...v1.34.2)

### Chores

* **tests:** skip some failing tests on the latest python versions ([ec77a0f](https://github.com/dodopayments/dodopayments-python/commit/ec77a0f9130b51d4992d18ad59260a9ac35456e6))

## 1.34.1 (2025-06-21)

Full Changelog: [v1.34.0...v1.34.1](https://github.com/dodopayments/dodopayments-python/compare/v1.34.0...v1.34.1)

### Features

* **client:** add support for aiohttp ([ff6068c](https://github.com/dodopayments/dodopayments-python/commit/ff6068c83742a492bd78888312976d79df35c34d))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([21e4aef](https://github.com/dodopayments/dodopayments-python/commit/21e4aef206be5ab337a2682c0833b2e850df1043))

## 1.34.0 (2025-06-18)

Full Changelog: [v1.32.0...v1.34.0](https://github.com/dodopayments/dodopayments-python/compare/v1.32.0...v1.34.0)

### Features

* **api:** updated to version 1.34.0 ([b83c3a8](https://github.com/dodopayments/dodopayments-python/commit/b83c3a87e253e3c74e9160ffe98d9b8fedaa8af1))


### Bug Fixes

* **client:** correctly parse binary response | stream ([4d41dc7](https://github.com/dodopayments/dodopayments-python/commit/4d41dc78632a83e98d91dd763858b61625d75cdc))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([10cf09b](https://github.com/dodopayments/dodopayments-python/commit/10cf09b005788fff2e01ec99d1ec70f71f09a80d))


### Chores

* **ci:** enable for pull requests ([ff898a1](https://github.com/dodopayments/dodopayments-python/commit/ff898a143cc3a7ce7ccccfc435f0af9a21f826d8))
* **internal:** update conftest.py ([c0c8eef](https://github.com/dodopayments/dodopayments-python/commit/c0c8eefc8e397aeb0933476ffd8b48c7ab9c0c72))
* **readme:** update badges ([6b1593c](https://github.com/dodopayments/dodopayments-python/commit/6b1593c2fe586d7fbabdeac3c7683fcad6256f63))
* **tests:** add tests for httpx client instantiation & proxies ([c7b0949](https://github.com/dodopayments/dodopayments-python/commit/c7b09497f1fe1f83bbd5a259174276a57ab7fafa))
* **tests:** run tests in parallel ([d46598b](https://github.com/dodopayments/dodopayments-python/commit/d46598b3cef4df023e692e84cb9265b7d9c8f22a))

## 1.32.0 (2025-06-09)

Full Changelog: [v1.30.2...v1.32.0](https://github.com/dodopayments/dodopayments-python/compare/v1.30.2...v1.32.0)

### Features

* **api:** updated openapi spec to v1.32.0 ([b482016](https://github.com/dodopayments/dodopayments-python/commit/b48201636b68d5b81d37b0e3eb00ccdf068f47f9))

## 1.30.2 (2025-06-04)

Full Changelog: [v1.30.0...v1.30.2](https://github.com/dodopayments/dodopayments-python/compare/v1.30.0...v1.30.2)

### Features

* **api:** fixed openapi spec ([15906d8](https://github.com/dodopayments/dodopayments-python/commit/15906d809eb6ab659e3b60ee1b5c92b3716c6730))
* **client:** add follow_redirects request option ([fb63495](https://github.com/dodopayments/dodopayments-python/commit/fb63495b183be3cbe1c4d0eacfdfaeb7f00653e0))


### Chores

* **docs:** remove reference to rye shell ([865a4ac](https://github.com/dodopayments/dodopayments-python/commit/865a4acfec4f830bc4209267a7d937dba0c401be))

## 1.30.0 (2025-06-02)

Full Changelog: [v1.27.0...v1.30.0](https://github.com/dodopayments/dodopayments-python/compare/v1.27.0...v1.30.0)

### Features

* **api:** manual updates ([7bd55ab](https://github.com/dodopayments/dodopayments-python/commit/7bd55ab6d9cf1671a0f5c5b38132a87a997fd25f))

## 1.27.0 (2025-05-26)

Full Changelog: [v1.25.0...v1.27.0](https://github.com/dodopayments/dodopayments-python/compare/v1.25.0...v1.27.0)

### Features

* **api:** added brands api in our sdk ([b8f73d6](https://github.com/dodopayments/dodopayments-python/commit/b8f73d6acc84c460cf208e0e3c810b55682f0b80))
* **api:** updated openapi spec to 1.27.0 ([80018eb](https://github.com/dodopayments/dodopayments-python/commit/80018eb91090140bb7c4336b8f6d9d0aae8db557))


### Chores

* **docs:** grammar improvements ([8aa60f1](https://github.com/dodopayments/dodopayments-python/commit/8aa60f1ca726282cc61bd573056f6bd1f8aaa51e))

## 1.25.0 (2025-05-17)

Full Changelog: [v1.22.0...v1.25.0](https://github.com/dodopayments/dodopayments-python/compare/v1.22.0...v1.25.0)

### Features

* **api:** updated openapi spec ([792e941](https://github.com/dodopayments/dodopayments-python/commit/792e941d70eea5d68c3aeaf6f62ece8e65e4d5e3))


### Bug Fixes

* **package:** support direct resource imports ([da506b9](https://github.com/dodopayments/dodopayments-python/commit/da506b990e1995b637b305b1a143f9b3450a1db3))


### Chores

* **ci:** fix installation instructions ([c41560f](https://github.com/dodopayments/dodopayments-python/commit/c41560f5419a74820bd8892fac39e965d4edbe3e))
* **ci:** upload sdks to package manager ([6644ed9](https://github.com/dodopayments/dodopayments-python/commit/6644ed959e12f46fc2a2d17efb712f21da0bdbe1))
* **internal:** codegen related update ([5169a98](https://github.com/dodopayments/dodopayments-python/commit/5169a98039143d54dd29016267bafb913095180f))
* **internal:** version bump ([eb5ca8a](https://github.com/dodopayments/dodopayments-python/commit/eb5ca8aed27afc7a2e85f0767713717fcc321e71))

## 1.22.0 (2025-05-09)

Full Changelog: [v1.21.0...v1.22.0](https://github.com/dodopayments/dodopayments-python/compare/v1.21.0...v1.22.0)

### Features

* **api:** updated openapi spec ([1387f36](https://github.com/dodopayments/dodopayments-python/commit/1387f36673bcffec0cc083d29134bcad55e1d7d1))


### Chores

* **internal:** avoid errors for isinstance checks on proxies ([a0adf04](https://github.com/dodopayments/dodopayments-python/commit/a0adf048949c53ab6cd6a8fe0f4153a6a99a4be3))

## 1.21.0 (2025-05-06)

Full Changelog: [v1.20.0...v1.21.0](https://github.com/dodopayments/dodopayments-python/compare/v1.20.0...v1.21.0)

### Features

* **api:** fixed api key schema to bearer ([ecaf908](https://github.com/dodopayments/dodopayments-python/commit/ecaf908a7f85b3909eb15081919f3112309c96ca))
* **api:** manual updates ([fe68093](https://github.com/dodopayments/dodopayments-python/commit/fe6809341aa15f8654bc14832374bb8161587104))

## 1.20.0 (2025-05-01)

Full Changelog: [v1.19.0...v1.20.0](https://github.com/dodopayments/dodopayments-python/compare/v1.19.0...v1.20.0)

### Features

* **api:** added addons ([645d6cc](https://github.com/dodopayments/dodopayments-python/commit/645d6cc31af0553aa94b936b9eee9a27681a378c))
* **api:** updated readme example ([ad59e88](https://github.com/dodopayments/dodopayments-python/commit/ad59e886826fb0366a20d99a6689ca93d93cc5b0))
* **api:** updated readme example ([bf3b943](https://github.com/dodopayments/dodopayments-python/commit/bf3b9434427b21cb8b3bd6214068ca6dccd18387))

## 1.19.0 (2025-04-30)

Full Changelog: [v1.18.3...v1.19.0](https://github.com/dodopayments/dodopayments-python/compare/v1.18.3...v1.19.0)

### Features

* **api:** manual updates ([021f4f3](https://github.com/dodopayments/dodopayments-python/commit/021f4f3c980395aecefd58480ffba0e4b0db5084))

## 1.18.3 (2025-04-25)

Full Changelog: [v1.18.1...v1.18.3](https://github.com/dodopayments/dodopayments-python/compare/v1.18.1...v1.18.3)

### Features

* **api:** manual updates ([5bb1c71](https://github.com/dodopayments/dodopayments-python/commit/5bb1c71da109ec82f06ee20c19c59ee1f77d8e80))

## 1.18.1 (2025-04-24)

Full Changelog: [v1.18.0...v1.18.1](https://github.com/dodopayments/dodopayments-python/compare/v1.18.0...v1.18.1)

### Chores

* broadly detect json family of content-type headers ([ea30879](https://github.com/dodopayments/dodopayments-python/commit/ea30879dfd6b18b4325f7759077e35dba4104ecf))
* **ci:** only use depot for staging repos ([55a7fd9](https://github.com/dodopayments/dodopayments-python/commit/55a7fd9838e52ee851eee7a588f8f356fc521754))
* **internal:** codegen related update ([bfcafe2](https://github.com/dodopayments/dodopayments-python/commit/bfcafe25fdc791b6384480ed8ac9e41dc17b7147))
* **internal:** minor formatting changes ([7c43392](https://github.com/dodopayments/dodopayments-python/commit/7c43392fececb07827c5fbca9df4e3aba4409354))

## 1.18.0 (2025-04-23)

Full Changelog: [v1.17.0...v1.18.0](https://github.com/dodopayments/dodopayments-python/compare/v1.17.0...v1.18.0)

### Features

* **api:** added change plan api ([f5e0221](https://github.com/dodopayments/dodopayments-python/commit/f5e02213139c65191452bf6281ec5f6cb8c4f6b4))
* **api:** manual updates ([e2cb784](https://github.com/dodopayments/dodopayments-python/commit/e2cb78486eda546f99b1783401e334fbdfa98c6d))


### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([6a4dc96](https://github.com/dodopayments/dodopayments-python/commit/6a4dc9681e696699a96b355e7389cbe24ce25733))


### Chores

* **ci:** add timeout thresholds for CI jobs ([c08ec1a](https://github.com/dodopayments/dodopayments-python/commit/c08ec1a3d6accde1a2cb828a2cebaab03aa7b753))
* **internal:** fix list file params ([eaadf56](https://github.com/dodopayments/dodopayments-python/commit/eaadf56084232a42029e07c647020ef70242f045))
* **internal:** import reformatting ([a8ba43d](https://github.com/dodopayments/dodopayments-python/commit/a8ba43dd8f46bad16ed2987f67399c252fb7d561))
* **internal:** refactor retries to not use recursion ([b8f7ac3](https://github.com/dodopayments/dodopayments-python/commit/b8f7ac34facfc3c1a7340aa3e247b29e5cb51809))

## 1.17.0 (2025-04-22)

Full Changelog: [v1.16.1...v1.17.0](https://github.com/dodopayments/dodopayments-python/compare/v1.16.1...v1.17.0)

### Features

* **api:** manual updates ([4f3a153](https://github.com/dodopayments/dodopayments-python/commit/4f3a15396b087d187355e51cc87a3b5d133bef4f))


### Chores

* **internal:** update models test ([8ff53b8](https://github.com/dodopayments/dodopayments-python/commit/8ff53b897756734133292987dab6fe0f20cd8b5e))

## 1.16.1 (2025-04-18)

Full Changelog: [v1.14.1...v1.16.1](https://github.com/dodopayments/dodopayments-python/compare/v1.14.1...v1.16.1)

### Features

* **api:** manual updates ([d1efa52](https://github.com/dodopayments/dodopayments-python/commit/d1efa52b1a20520fce22f7876561361376210056))

## 1.14.1 (2025-04-17)

Full Changelog: [v1.14.0...v1.14.1](https://github.com/dodopayments/dodopayments-python/compare/v1.14.0...v1.14.1)

### Bug Fixes

* **perf:** optimize some hot paths ([14b4eb6](https://github.com/dodopayments/dodopayments-python/commit/14b4eb67b69bc844cc230ad98acb11fb67019fcb))
* **perf:** skip traversing types for NotGiven values ([a58ba0e](https://github.com/dodopayments/dodopayments-python/commit/a58ba0e05ab326c840f266524a51c33befe5ce87))


### Chores

* **client:** minor internal fixes ([ca2a33e](https://github.com/dodopayments/dodopayments-python/commit/ca2a33ebfda183f80945ee79438f7cf91e434050))
* **internal:** base client updates ([f833a1f](https://github.com/dodopayments/dodopayments-python/commit/f833a1f1480c86fb3df8f473ff54e3abe6c0c2f6))
* **internal:** bump pyright version ([2b2c993](https://github.com/dodopayments/dodopayments-python/commit/2b2c9933a6fb65ff6798ee689308f8383fd3b1a8))
* **internal:** update pyright settings ([66c956f](https://github.com/dodopayments/dodopayments-python/commit/66c956f007c7fa00ff1c525a05253f1dce9921b9))

## 1.14.0 (2025-04-11)

Full Changelog: [v1.13.0...v1.14.0](https://github.com/dodopayments/dodopayments-python/compare/v1.13.0...v1.14.0)

### Features

* **api:** fixed license key pagination issues in openapi spec ([537ec87](https://github.com/dodopayments/dodopayments-python/commit/537ec87a279e8ad28df4cc72437237a4ba3d3d28))
* **api:** updated openapi spec ([64b978a](https://github.com/dodopayments/dodopayments-python/commit/64b978ad6113409a30318535f36c95c9db34bc70))


### Chores

* **internal:** expand CI branch coverage ([6b90baf](https://github.com/dodopayments/dodopayments-python/commit/6b90baf9e0454e117537737944949fe47d2fe50d))
* **internal:** reduce CI branch coverage ([1466ee2](https://github.com/dodopayments/dodopayments-python/commit/1466ee25d33cd01029d682491f66f578e6d98f6b))
* **internal:** slight transform perf improvement ([#120](https://github.com/dodopayments/dodopayments-python/issues/120)) ([36e9378](https://github.com/dodopayments/dodopayments-python/commit/36e9378ae36a901a6cf681e04334485b518087d3))

## 1.13.0 (2025-04-08)

Full Changelog: [v1.11.1...v1.13.0](https://github.com/dodopayments/dodopayments-python/compare/v1.11.1...v1.13.0)

### Features

* **api:** manual updates ([#118](https://github.com/dodopayments/dodopayments-python/issues/118)) ([f871019](https://github.com/dodopayments/dodopayments-python/commit/f871019a47a032f9d0ef45229bfa4e10d396ae86))

## 1.11.1 (2025-04-05)

Full Changelog: [v1.11.0...v1.11.1](https://github.com/dodopayments/dodopayments-python/compare/v1.11.0...v1.11.1)

### Chores

* **internal:** remove trailing character ([#116](https://github.com/dodopayments/dodopayments-python/issues/116)) ([bf80473](https://github.com/dodopayments/dodopayments-python/commit/bf8047310a09bd4e6d166155f697cf17e069dabb))

## 1.11.0 (2025-03-28)

Full Changelog: [v1.10.4...v1.11.0](https://github.com/dodopayments/dodopayments-python/compare/v1.10.4...v1.11.0)

### Features

* **api:** manual updates ([#112](https://github.com/dodopayments/dodopayments-python/issues/112)) ([c6aeb2d](https://github.com/dodopayments/dodopayments-python/commit/c6aeb2def1fc7dc58195e17506339b89fde183f7))

## 1.10.4 (2025-03-28)

Full Changelog: [v1.10.3...v1.10.4](https://github.com/dodopayments/dodopayments-python/compare/v1.10.3...v1.10.4)

### Chores

* fix typos ([#109](https://github.com/dodopayments/dodopayments-python/issues/109)) ([e48aa30](https://github.com/dodopayments/dodopayments-python/commit/e48aa30b98c92749cde5bc322aaf2b4e181eecdc))

## 1.10.3 (2025-03-25)

Full Changelog: [v1.10.1...v1.10.3](https://github.com/dodopayments/dodopayments-python/compare/v1.10.1...v1.10.3)

### Features

* **api:** manual updates ([#106](https://github.com/dodopayments/dodopayments-python/issues/106)) ([e5e6a8e](https://github.com/dodopayments/dodopayments-python/commit/e5e6a8e808ea2af7cad06c9f3defab20e8c7893a))

## 1.10.1 (2025-03-21)

Full Changelog: [v1.7.0...v1.10.1](https://github.com/dodopayments/dodopayments-python/compare/v1.7.0...v1.10.1)

### Features

* **api:** updated openapispec to v1.10.1 ([#104](https://github.com/dodopayments/dodopayments-python/issues/104)) ([1ddc877](https://github.com/dodopayments/dodopayments-python/commit/1ddc8773fccb48071a357b8f43125b8a5d525263))


### Bug Fixes

* **ci:** ensure pip is always available ([#102](https://github.com/dodopayments/dodopayments-python/issues/102)) ([30b1832](https://github.com/dodopayments/dodopayments-python/commit/30b183260b211be3de0b7c06a3209b15bd4811e2))
* **ci:** remove publishing patch ([#103](https://github.com/dodopayments/dodopayments-python/issues/103)) ([c95e804](https://github.com/dodopayments/dodopayments-python/commit/c95e80468aa607f4a41434244db9f8414365e187))
* **types:** handle more discriminated union shapes ([#101](https://github.com/dodopayments/dodopayments-python/issues/101)) ([701dc57](https://github.com/dodopayments/dodopayments-python/commit/701dc577c04a4564a7e6f667499c40007e90b53a))


### Chores

* **internal:** bump rye to 0.44.0 ([#100](https://github.com/dodopayments/dodopayments-python/issues/100)) ([0ae8ed3](https://github.com/dodopayments/dodopayments-python/commit/0ae8ed354740d966c7c9f63e027896b47610d84b))
* **internal:** codegen related update ([#98](https://github.com/dodopayments/dodopayments-python/issues/98)) ([0a8df0a](https://github.com/dodopayments/dodopayments-python/commit/0a8df0a0c10514547ea6cf594cc6a4b1830c679a))

## 1.7.0 (2025-03-14)

Full Changelog: [v1.6.3...v1.7.0](https://github.com/dodopayments/dodopayments-python/compare/v1.6.3...v1.7.0)

### Features

* **api:** fixed openapi spec issues ([#95](https://github.com/dodopayments/dodopayments-python/issues/95)) ([3500cdf](https://github.com/dodopayments/dodopayments-python/commit/3500cdf48057d4b73f101ca7a9c34a99c767b407))

## 1.6.3 (2025-03-14)

Full Changelog: [v1.5.1...v1.6.3](https://github.com/dodopayments/dodopayments-python/compare/v1.5.1...v1.6.3)

### Features

* **api:** openapi spec updated ([#92](https://github.com/dodopayments/dodopayments-python/issues/92)) ([1f75653](https://github.com/dodopayments/dodopayments-python/commit/1f75653005e0325012368b947ff7639073969320))
* **api:** updated stainless config ([#93](https://github.com/dodopayments/dodopayments-python/issues/93)) ([8f8ad45](https://github.com/dodopayments/dodopayments-python/commit/8f8ad45c2f193774ff492859c6165a1ca5092d6d))


### Chores

* **internal:** remove extra empty newlines ([#90](https://github.com/dodopayments/dodopayments-python/issues/90)) ([0b43ad9](https://github.com/dodopayments/dodopayments-python/commit/0b43ad9b63cd881955ce8a7729436bcb118966b5))

## 1.5.1 (2025-03-12)

Full Changelog: [v1.5.0...v1.5.1](https://github.com/dodopayments/dodopayments-python/compare/v1.5.0...v1.5.1)

### Chores

* **internal:** codegen related update ([#87](https://github.com/dodopayments/dodopayments-python/issues/87)) ([80c7a0c](https://github.com/dodopayments/dodopayments-python/commit/80c7a0c288f4a8c30277af352bb2926e5080bd1a))

## 1.5.0 (2025-03-07)

Full Changelog: [v1.0.0...v1.5.0](https://github.com/dodopayments/dodopayments-python/compare/v1.0.0...v1.5.0)

### Features

* **api:** manual updates ([#85](https://github.com/dodopayments/dodopayments-python/issues/85)) ([43fba1d](https://github.com/dodopayments/dodopayments-python/commit/43fba1d0e01dacaf5a36f2322aaf658662475ec4))


### Chores

* **docs:** update client docstring ([#83](https://github.com/dodopayments/dodopayments-python/issues/83)) ([9634005](https://github.com/dodopayments/dodopayments-python/commit/96340059bb7d80ab7334bb68986a8758b0d12399))
* **internal:** properly set __pydantic_private__ ([#80](https://github.com/dodopayments/dodopayments-python/issues/80)) ([b7501ec](https://github.com/dodopayments/dodopayments-python/commit/b7501ecd3854a02d4e9117ce45b96a315521eb4d))
* **internal:** remove unused http client options forwarding ([#84](https://github.com/dodopayments/dodopayments-python/issues/84)) ([650c31e](https://github.com/dodopayments/dodopayments-python/commit/650c31e52294fbe96b9ba75f553d2dad0657ac18))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#82](https://github.com/dodopayments/dodopayments-python/issues/82)) ([ccf6dbb](https://github.com/dodopayments/dodopayments-python/commit/ccf6dbb0147fd5f1e108270d9867cd27f0b5963b))

## 1.0.0 (2025-02-23)

Full Changelog: [v0.24.0...v1.0.0](https://github.com/dodopayments/dodopayments-python/compare/v0.24.0...v1.0.0)

### Features

* **api:** fixed errors ([#78](https://github.com/dodopayments/dodopayments-python/issues/78)) ([d462ea1](https://github.com/dodopayments/dodopayments-python/commit/d462ea18b8782ac238923153aac010c0b80e5bb6))
* **api:** updated config and updated version to v1.0.0 ([#77](https://github.com/dodopayments/dodopayments-python/issues/77)) ([dc95e7e](https://github.com/dodopayments/dodopayments-python/commit/dc95e7ee5c09489fbd9c8085c52a63fffb9684d2))
* **client:** allow passing `NotGiven` for body ([#74](https://github.com/dodopayments/dodopayments-python/issues/74)) ([ae70adb](https://github.com/dodopayments/dodopayments-python/commit/ae70adb726dbd99229cf61f4bab2be6b4c423496))


### Bug Fixes

* **client:** mark some request bodies as optional ([ae70adb](https://github.com/dodopayments/dodopayments-python/commit/ae70adb726dbd99229cf61f4bab2be6b4c423496))


### Chores

* **internal:** fix devcontainers setup ([#76](https://github.com/dodopayments/dodopayments-python/issues/76)) ([e5e7fbd](https://github.com/dodopayments/dodopayments-python/commit/e5e7fbdbc803b4ec4b12053f5b759228a1e6d3bf))

## 0.24.0 (2025-02-15)

Full Changelog: [v0.22.1...v0.24.0](https://github.com/dodopayments/dodopayments-python/compare/v0.22.1...v0.24.0)

### Features

* **api:** added discount apis ([#72](https://github.com/dodopayments/dodopayments-python/issues/72)) ([13430e4](https://github.com/dodopayments/dodopayments-python/commit/13430e4e64319f2187b225fe887a4bf226609620))
* **api:** openapi spec changes ([#71](https://github.com/dodopayments/dodopayments-python/issues/71)) ([d61ebfc](https://github.com/dodopayments/dodopayments-python/commit/d61ebfc0bb7f9d49cca167ac10abda28f9b944c3))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#70](https://github.com/dodopayments/dodopayments-python/issues/70)) ([bd7bda1](https://github.com/dodopayments/dodopayments-python/commit/bd7bda13fcc21c155e631a67e3f604a5ccdba2fb))


### Chores

* **internal:** update client tests ([#68](https://github.com/dodopayments/dodopayments-python/issues/68)) ([640f46a](https://github.com/dodopayments/dodopayments-python/commit/640f46a514b24a3594fc8ec52d78a889c22ccdbf))

## 0.22.1 (2025-02-11)

Full Changelog: [v0.22.0...v0.22.1](https://github.com/dodopayments/dodopayments-python/compare/v0.22.0...v0.22.1)

### Features

* **api:** manual updates ([#66](https://github.com/dodopayments/dodopayments-python/issues/66)) ([ebd4c53](https://github.com/dodopayments/dodopayments-python/commit/ebd4c533852f3f63aad48f8e1efc5a1185bf01d2))


### Chores

* **internal:** fix type traversing dictionary params ([#63](https://github.com/dodopayments/dodopayments-python/issues/63)) ([1927cd8](https://github.com/dodopayments/dodopayments-python/commit/1927cd8f3e744c57d9c47d8a8dfd55823a7aa524))
* **internal:** minor type handling changes ([#65](https://github.com/dodopayments/dodopayments-python/issues/65)) ([c516f36](https://github.com/dodopayments/dodopayments-python/commit/c516f36044abdfc180cba62e3cb9b07ef1edf54e))

## 0.22.0 (2025-02-06)

Full Changelog: [v0.20.2...v0.22.0](https://github.com/dodopayments/dodopayments-python/compare/v0.20.2...v0.22.0)

### Features

* **api:** updated API changes for v0.22.0 ([#61](https://github.com/dodopayments/dodopayments-python/issues/61)) ([cffb009](https://github.com/dodopayments/dodopayments-python/commit/cffb009c740851df8c0547c6d0bac70f423b6e57))
* **client:** send `X-Stainless-Read-Timeout` header ([#59](https://github.com/dodopayments/dodopayments-python/issues/59)) ([c03b692](https://github.com/dodopayments/dodopayments-python/commit/c03b6922a2d17b5dd1034397ed30a311ab7a70ae))

## 0.20.2 (2025-02-04)

Full Changelog: [v0.20.1...v0.20.2](https://github.com/dodopayments/dodopayments-python/compare/v0.20.1...v0.20.2)

### Chores

* **internal:** bummp ruff dependency ([#57](https://github.com/dodopayments/dodopayments-python/issues/57)) ([e5c6363](https://github.com/dodopayments/dodopayments-python/commit/e5c6363eee138fbb9ef0ccf02f42a66be9fa76cd))
* **internal:** change default timeout to an int ([#55](https://github.com/dodopayments/dodopayments-python/issues/55)) ([6ca033c](https://github.com/dodopayments/dodopayments-python/commit/6ca033c12b8fec8bfe27098953aca9ab76a41a05))

## 0.20.1 (2025-01-29)

Full Changelog: [v0.19.0...v0.20.1](https://github.com/dodopayments/dodopayments-python/compare/v0.19.0...v0.20.1)

### Features

* **api:** manual updates ([#53](https://github.com/dodopayments/dodopayments-python/issues/53)) ([612e586](https://github.com/dodopayments/dodopayments-python/commit/612e586258b5e266445a2a1d685ff72be8af3181))


### Chores

* **internal:** minor formatting changes ([#51](https://github.com/dodopayments/dodopayments-python/issues/51)) ([e870ddc](https://github.com/dodopayments/dodopayments-python/commit/e870ddc3d4e57cb72a043594f0dd4641f541b4ab))

## 0.19.0 (2025-01-23)

Full Changelog: [v0.18.0...v0.19.0](https://github.com/dodopayments/dodopayments-python/compare/v0.18.0...v0.19.0)

### Features

* **api:** added archive product api ([#42](https://github.com/dodopayments/dodopayments-python/issues/42)) ([b093037](https://github.com/dodopayments/dodopayments-python/commit/b09303799ac6153e20534a202c108640d14d82b1))
* **api:** manual updates ([#48](https://github.com/dodopayments/dodopayments-python/issues/48)) ([ebcb3a5](https://github.com/dodopayments/dodopayments-python/commit/ebcb3a540465007939522f6dddccfbe58b1b59b2))
* **api:** manual updates ([#49](https://github.com/dodopayments/dodopayments-python/issues/49)) ([320d3ed](https://github.com/dodopayments/dodopayments-python/commit/320d3ed891ad7f5244571670ca3bc47041de3b9e))


### Bug Fixes

* **tests:** make test_get_platform less flaky ([#45](https://github.com/dodopayments/dodopayments-python/issues/45)) ([17adaaf](https://github.com/dodopayments/dodopayments-python/commit/17adaaf1617cbac71b4413d9ec08e5b6ae4b3478))


### Chores

* **internal:** avoid pytest-asyncio deprecation warning ([#46](https://github.com/dodopayments/dodopayments-python/issues/46)) ([1fefc76](https://github.com/dodopayments/dodopayments-python/commit/1fefc768a47d7823382423fec935c145c14d8297))
* **internal:** minor style changes ([#47](https://github.com/dodopayments/dodopayments-python/issues/47)) ([588dfcf](https://github.com/dodopayments/dodopayments-python/commit/588dfcf5080c95dfaf4976c1c8344e7c0d3da375))


### Documentation

* **raw responses:** fix duplicate `the` ([#44](https://github.com/dodopayments/dodopayments-python/issues/44)) ([fd97103](https://github.com/dodopayments/dodopayments-python/commit/fd9710387f3f27bcc6e783bc59dcec63a2f3dc31))

## 0.18.0 (2025-01-20)

Full Changelog: [v0.17.0...v0.18.0](https://github.com/dodopayments/dodopayments-python/compare/v0.17.0...v0.18.0)

### Features

* **api:** updated openapi sepc ([#40](https://github.com/dodopayments/dodopayments-python/issues/40)) ([290c0fe](https://github.com/dodopayments/dodopayments-python/commit/290c0fed5eb1ea9dfb6ebce62e9ec89abe59c1f0))


### Chores

* **internal:** codegen related update ([#38](https://github.com/dodopayments/dodopayments-python/issues/38)) ([2676646](https://github.com/dodopayments/dodopayments-python/commit/267664605d16126654c64f501bd828d7494f84b1))

## 0.17.0 (2025-01-16)

Full Changelog: [v0.16.1...v0.17.0](https://github.com/dodopayments/dodopayments-python/compare/v0.16.1...v0.17.0)

### Features

* **api:** added filter apis ([#35](https://github.com/dodopayments/dodopayments-python/issues/35)) ([75dcbe4](https://github.com/dodopayments/dodopayments-python/commit/75dcbe42b1c2404b849b0729925142f8c75ef8d7))

## 0.16.1 (2025-01-11)

Full Changelog: [v0.15.1...v0.16.1](https://github.com/dodopayments/dodopayments-python/compare/v0.15.1...v0.16.1)

### Features

* **api:** updated openapi spec ([#33](https://github.com/dodopayments/dodopayments-python/issues/33)) ([9a99304](https://github.com/dodopayments/dodopayments-python/commit/9a99304bbe47ba3a37fec11ddc635e02b6e1dd9b))


### Bug Fixes

* **client:** only call .close() when needed ([#29](https://github.com/dodopayments/dodopayments-python/issues/29)) ([da78ed6](https://github.com/dodopayments/dodopayments-python/commit/da78ed69d8bc4d6407f58ae260088b8f8df91241))
* correctly handle deserialising `cls` fields ([#32](https://github.com/dodopayments/dodopayments-python/issues/32)) ([db7377e](https://github.com/dodopayments/dodopayments-python/commit/db7377e9f0dc450ac9a78277da7fccde152f57da))


### Chores

* add missing isclass check ([#26](https://github.com/dodopayments/dodopayments-python/issues/26)) ([359e5aa](https://github.com/dodopayments/dodopayments-python/commit/359e5aaf9a6ef61b0a702c37b4ded51ead5d39b8))
* **internal:** codegen related update ([#28](https://github.com/dodopayments/dodopayments-python/issues/28)) ([5aeb091](https://github.com/dodopayments/dodopayments-python/commit/5aeb091907bf7a0ad139e80c775d14a5fe2e36c8))
* **internal:** codegen related update ([#31](https://github.com/dodopayments/dodopayments-python/issues/31)) ([9b5422d](https://github.com/dodopayments/dodopayments-python/commit/9b5422d94547ca59f9e9b4408c5162df1319c32d))


### Documentation

* fix typos ([#30](https://github.com/dodopayments/dodopayments-python/issues/30)) ([5d18f17](https://github.com/dodopayments/dodopayments-python/commit/5d18f17ce1894d99d139b2889908b6741ba75de6))

## 0.15.1 (2025-01-03)

Full Changelog: [v0.14.1...v0.15.1](https://github.com/dodopayments/dodopayments-python/compare/v0.14.1...v0.15.1)

### Features

* **api:** added invoice api and update openapi spec ([#24](https://github.com/dodopayments/dodopayments-python/issues/24)) ([2f38610](https://github.com/dodopayments/dodopayments-python/commit/2f38610150d623de7594496a3657407aaf027c07))


### Chores

* **internal:** codegen related update ([#22](https://github.com/dodopayments/dodopayments-python/issues/22)) ([853417d](https://github.com/dodopayments/dodopayments-python/commit/853417d938d024c8f9e350e62a38477d36677e13))

## 0.14.1 (2024-12-29)

Full Changelog: [v0.14.0...v0.14.1](https://github.com/dodopayments/dodopayments-python/compare/v0.14.0...v0.14.1)

### Features

* **api:** manual updates ([#19](https://github.com/dodopayments/dodopayments-python/issues/19)) ([563c121](https://github.com/dodopayments/dodopayments-python/commit/563c1212dd74c708b7d382c6e9f902d6964d3c23))

## 0.14.0 (2024-12-25)

Full Changelog: [v0.13.2...v0.14.0](https://github.com/dodopayments/dodopayments-python/compare/v0.13.2...v0.14.0)

### Features

* **api:** updated openapi spec for License Keys ([#16](https://github.com/dodopayments/dodopayments-python/issues/16)) ([56e841b](https://github.com/dodopayments/dodopayments-python/commit/56e841b7d506da6f1967f63b5ec5425c0771ce92))

## 0.13.2 (2024-12-21)

Full Changelog: [v0.12.0...v0.13.2](https://github.com/dodopayments/dodopayments-python/compare/v0.12.0...v0.13.2)

### Chores

* **internal:** fix some typos ([#13](https://github.com/dodopayments/dodopayments-python/issues/13)) ([9992490](https://github.com/dodopayments/dodopayments-python/commit/99924907412f2e80b4c7b84650495e27a9a879a1))

## 0.12.0 (2024-12-17)

Full Changelog: [v0.11.1...v0.12.0](https://github.com/dodopayments/dodopayments-python/compare/v0.11.1...v0.12.0)

### Features

* **api:** api update ([#8](https://github.com/dodopayments/dodopayments-python/issues/8)) ([77cf406](https://github.com/dodopayments/dodopayments-python/commit/77cf406ce935a51c381e19a6a427749e585c4def))
* **api:** updated openapi methods ([#11](https://github.com/dodopayments/dodopayments-python/issues/11)) ([de9e970](https://github.com/dodopayments/dodopayments-python/commit/de9e970593dd95881a9dc2806e7384e10a4cddbe))


### Chores

* **internal:** codegen related update ([#10](https://github.com/dodopayments/dodopayments-python/issues/10)) ([043abd0](https://github.com/dodopayments/dodopayments-python/commit/043abd0050b67ea4fe271c79f546922740c46c0e))

## 0.11.1 (2024-12-16)

Full Changelog: [v0.11.0...v0.11.1](https://github.com/dodopayments/dodopayments-python/compare/v0.11.0...v0.11.1)

### Features

* **api:** manual updates ([#5](https://github.com/dodopayments/dodopayments-python/issues/5)) ([c9fc026](https://github.com/dodopayments/dodopayments-python/commit/c9fc026d3e229c37c7d8bfb87189f9841cf2ece7))

## 0.11.0 (2024-12-16)

Full Changelog: [v0.0.1-alpha.0...v0.11.0](https://github.com/dodopayments/dodopayments-python/compare/v0.0.1-alpha.0...v0.11.0)

### Features

* **api:** update via SDK Studio ([26a2d8b](https://github.com/dodopayments/dodopayments-python/commit/26a2d8b386155eda8e36ca7cd8c932997f76fa5c))
* **api:** update via SDK Studio ([9e9a8e7](https://github.com/dodopayments/dodopayments-python/commit/9e9a8e74538ba1de3cf3dbeeaeb0cbc9f3e7c43b))
* **api:** update via SDK Studio ([6f936f7](https://github.com/dodopayments/dodopayments-python/commit/6f936f74ec25259b59094dff239f7f64573e9ff3))
* **api:** update via SDK Studio ([bc0ceee](https://github.com/dodopayments/dodopayments-python/commit/bc0ceee97417a2838dc2027c5f3d6d47f8946e8f))
* **api:** update via SDK Studio ([9e3e121](https://github.com/dodopayments/dodopayments-python/commit/9e3e121d1e860ec91a9aa691e1f054edb2eb115c))
* **api:** update via SDK Studio ([fc0dbfe](https://github.com/dodopayments/dodopayments-python/commit/fc0dbfe7c4cc9d6199402bbb90f70d6e2ce8440d))
* **api:** update via SDK Studio ([39689b9](https://github.com/dodopayments/dodopayments-python/commit/39689b9b26cc01bb3b8890d7a7c7f3b0bf4445cd))
* **api:** update via SDK Studio ([dd36b5e](https://github.com/dodopayments/dodopayments-python/commit/dd36b5e5869f5f6ef5264ed20529a37ea4016fc0))


### Chores

* go live ([#1](https://github.com/dodopayments/dodopayments-python/issues/1)) ([6786737](https://github.com/dodopayments/dodopayments-python/commit/6786737914b7f2a36250ef8c2754d405b96a809d))
* **internal:** add support for TypeAliasType ([1d86b93](https://github.com/dodopayments/dodopayments-python/commit/1d86b9379e348777362a0e67334344e7a237032b))
* **internal:** bump pyright ([175e696](https://github.com/dodopayments/dodopayments-python/commit/175e6961135f0d4cddb5621b37744f60d30b19ce))
* **internal:** codegen related update ([cb7a979](https://github.com/dodopayments/dodopayments-python/commit/cb7a9791834d976f66e9bd6caa944d5a495917ee))
* **internal:** codegen related update ([19d85bf](https://github.com/dodopayments/dodopayments-python/commit/19d85bf829707326a0ea40a59d78ce72f101c153))
* **internal:** updated imports ([6894776](https://github.com/dodopayments/dodopayments-python/commit/6894776d2f1d7e546db913679379902a5742dd7f))
* update SDK settings ([#3](https://github.com/dodopayments/dodopayments-python/issues/3)) ([f0311ea](https://github.com/dodopayments/dodopayments-python/commit/f0311eaa1ba3ca4b892af4432345a852fc8215fe))
