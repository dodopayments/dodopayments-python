# Changelog

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
