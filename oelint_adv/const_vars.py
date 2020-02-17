
MANDATORY_VARS = [
    "SUMMARY",
    "DESCRIPTION",
    "AUTHOR",
    "HOMEPAGE",
    "SECTION",
    "LICENSE",
    "SRC_URI"
]

SUGGESTED_VARS = [
    "BUGTRACKER",
    "BBCLASSEXTEND",
    "CVE_PRODUCT"
]

VAR_ORDER = [
    "SUMMARY",
    "DESCRIPTION",
    "AUTHOR",
    "HOMEPAGE",
    "BUGTRACKER",
    "SECTION",
    "LICENSE",
    "LIC_FILES_CHKSUM",
    "DEPENDS",
    "PROVIDES",
    "PV",
    "SRC_URI",
    "SRCREV",
    "S",
    "inherit",
    "PACKAGECONFIG",
    "EXTRA_QMAKEVARS_POST",
    "EXTRA_OECONF",
    "PACKAGE_ARCH",
    "PACKAGES",
    "FILES_${PN}",
    "RDEPENDS_${PN}",
    "RRECOMMENDS_${PN}",
    "RSUGGESTS_${PN}",
    "RPROVIDES_${PN}",
    "RCONFLICTS_${PN}",
    "BBCLASSEXTEND"
]

KNOWN_VARS = [
    "ABIEXTENSION",
    "ALL_MULTILIB_PACKAGE_ARCHS",
    "ALL_QA",
    "ALTERNATIVE_PRIORITY",
    "ANY_OF_DISTRO_FEATURES",
    "APACHE_MIRROR",
    "APPEND",
    "ARCH_DEFAULT_KERNELIMAGETYPE",
    "ASNEEDED",
    "ASSUME_PROVIDED",
    "AUTO_LIBNAME_PKGS",
    "AUTOREV",
    "AVAILTUNES",
    "B",
    "BAD_RECOMMENDATIONS",
    "BASE_DEFAULT_DEPS",
    "BASE_GOARM",
    "BASE_WORKDIR",
    "BASEDEPENDS",
    "BASELIB",
    "BB_CMDLINE",
    "BB_CONSOLELOG",
    "BB_CURRENT_MC",
    "BB_DEFAULT_TASK",
    "BB_DISKMON_DIRS",
    "BB_ENV_EXTRAWHITE",
    "BB_GENERATE_MIRROR_TARBALLS",
    "BB_HASHBASE_WHITELIST",
    "BB_HASHCHECK_FUNCTION",
    "BB_HASHCONFIG_WHITELIST",
    "BB_HASHFILENAME",
    "BB_MIN_VERSION",
    "BB_NUMBER_THREADS",
    "BB_ORIGENV",
    "BB_SCHEDULER",
    "BB_SETSCENE_DEPVALID",
    "BB_SIGNATURE_EXCLUDE_FLAGS",
    "BB_SIGNATURE_HANDLER",
    "BB_STRICT_CHECKSUM",
    "BB_UNIHASH",
    "BB_VERSION",
    "BBFILE_COLLECTIONS",
    "BBFILES_DYNAMIC",
    "BBFILES",
    "BBINCLUDED",
    "BBINCLUDELOGS",
    "BBLAYERS_CONF_UPDATE_FUNCS",
    "BBLAYERS_FETCH_DIR",
    "BBLAYERS_LAYERINDEX_URL",
    "BBLAYERS",
    "BBPATH",
    "BINUVERSION",
    "BP",
    "BPN",
    "BUGTRACKER",
    "BUILD_ARCH",
    "BUILD_AS_ARCH",
    "BUILD_CC_ARCH",
    "BUILD_CFLAGS",
    "BUILD_CXXFLAGS",
    "BUILD_EXEEXT",
    "BUILD_GOARCH",
    "BUILD_GOOS",
    "BUILD_GOTUPLE",
    "BUILD_LD_ARCH",
    "BUILD_OPTIMIZATION",
    "BUILD_OS",
    "BUILD_PREFIX",
    "BUILD_SYS",
    "BUILD_VENDOR",
    "BUILDCFG_FUNCS",
    "BUILDCFG_HEADER",
    "BUILDCFG_NEEDEDVARS",
    "BUILDCFG_VARS",
    "BUILDSDK_CFLAGS",
    "BUILDSDK_CPPFLAGS",
    "BUILDSDK_CXXFLAGS",
    "BUILDSDK_LDFLAGS",
    "BUILDSTATS_BASE",
    "BUSYBOX_SPLIT_SUID",
    "CACHE",
    "CCACHE_DISABLE",
    "CCACHE",
    "CHRPATH_BIN",
    "CLANGSDK",
    "CLASSOVERRIDE",
    "CLEANBROKEN",
    "CLEANFUNCS",
    "CMDLINE",
    "COMBINED_FEATURES",
    "COMMERCIAL_AUDIO_PLUGINS",
    "COMMERCIAL_VIDEO_PLUGINS",
    "COMMON_LICENSE_DIR",
    "COMPATIBLE_MACHINE",
    "COMPILER_RT",
    "COMPONENTS_DIR",
    "COMPRESSIONTYPES",
    "CONF_VERSION",
    "CONFIG_EXTRA_CFLAGS",
    "CONFIG_FDISK_SUPPORT_LARGE_DISKS",
    "CONFIG_LFS",
    "CONFIGURESTAMPFILE",
    "CONLOG",
    "CONNECTIVITY_CHECK_URIS",
    "CONVERSIONTYPES",
    "CORE_IMAGE_BASE_INSTALL",
    "CORE_IMAGE_EXTRA_INSTALL",
    "COREBASE_FILES",
    "COREBASE",
    "CPAN_MIRROR",
    "CROSS_CURSES_INC",
    "CROSS_CURSES_LIB",
    "CVE_PRODUCT",
    "D",
    "DATA_LICENSE",
    "DATE",
    "DATETIME",
    "DEBIAN_MIRROR",
    "DEBIAN_NAMES",
    "DEBIANRDEP",
    "DEBUG_FLAGS",
    "DEBUG_OPTIMIZATION",
    "DEBUG_PREFIX_MAP",
    "DEFAULT_TASK_PROVIDER",
    "DEFAULTTUNE",
    "DEPCHAIN_POST",
    "DEPCHAIN_PRE",
    "DEPENDS_GOLANG",
    "DEPENDS",
    "DEPLOY_DIR_DEB",
    "DEPLOY_DIR_IMAGE",
    "DEPLOY_DIR_IPK",
    "DEPLOY_DIR_RPM",
    "DEPLOY_DIR_TAR",
    "DEPLOY_DIR_TOOLS",
    "DEPLOY_DIR",
    "DEPLOYABLE_IMAGE_TYPES",
    "DEPLOYDIR",
    "DESCRIPTION",
    "DEVSHELL_STARTDIR",
    "DEVSHELL",
    "DISABLE_STATIC",
    "DISTRO_CODENAME",
    "DISTRO_EXTRA_RDEPENDS",
    "DISTRO_EXTRA_RRECOMMENDS",
    "DISTRO_FEATURES_BACKFILL_CONSIDERED",
    "DISTRO_FEATURES_BACKFILL",
    "DISTRO_FEATURES_DEFAULT",
    "DISTRO_FEATURES_FILTER_NATIVE",
    "DISTRO_FEATURES_FILTER_NATIVESDK",
    "DISTRO_FEATURES_NATIVE",
    "DISTRO_FEATURES_NATIVESDK",
    "DISTRO_FEATURES",
    "DISTRO_NAME",
    "DISTRO_VERSION",
    "DISTROOVERRIDES",
    "DL_DIR",
    "ENABLE_BINARY_LOCALE_GENERATION",
    "ERROR_QA",
    "EXCLUDE_FROM_WORLD",
    "EXCONFIG_ARGS",
    "EXTENDPE",
    "EXTENDPKGEVER",
    "EXTENDPKGV",
    "EXTENDPRAUTO",
    "EXTRA_AUTORECONF",
    "EXTRA_IMAGE_FEATURES",
    "EXTRA_IMAGECMD",
    "EXTRA_IMAGEDEPENDS",
    "EXTRA_NATIVE_PKGCONFIG_PATH",
    "EXTRA_OECMAKE",
    "EXTRA_OECONF",
    "EXTRA_OEMAKE",
    "EXTRA_OEMAKEINST",
    "EXTRA_OEMESON",
    "EXTRA_OESCONS",
    "EXTRA_STAGING_FIXMES",
    "EXTRANATIVEPATH",
    "EXTRAOPKGCONFIG",
    "FAKEROOT_QA",
    "FAKEROOTBASEENV",
    "FAKEROOTCMD",
    "FAKEROOTDIRS",
    "FAKEROOTENV",
    "FAKEROOTNOENV",
    "FEATURE_INSTALL_OPTIONAL",
    "FEATURE_INSTALL",
    "FILE_DIRNAME",
    "FILE",
    "FILES_SOLIBSDEV",
    "FILES",
    "FILESEXTRAPATHS",
    "FILESOVERRIDES",
    "FILESPATH",
    "FILESYSTEM_PERMS_TABLES",
    "FOSS_BASE_URL",
    "FOSS_FULL_SPDX",
    "FOSS_NO_COPYRIGHT",
    "FOSS_RECURSIVE_UNPACK",
    "FOSS_SERVER",
    "FOSS_WGET_FLAGS",
    "FULL_OPTIMIZATION",
    "GCCPIE",
    "GCCVERSION",
    "GDBVERSION",
    "GENTOO_MIRROR",
    "GLIBCVERSION",
    "GNOME_GIT",
    "GNOME_MIRROR",
    "GNU_MIRROR",
    "GNUPG_MIRROR",
    "GO_BUILD_BINDIR",
    "GO_DYNLINK",
    "GO_EXTLDFLAGS",
    "GO_IMPORT",
    "GO_INSTALL_FILTEROUT",
    "GO_INSTALL",
    "GO_LDFLAGS",
    "GO_LINKMODE",
    "GO_LINKSHARED",
    "GO_PARALLEL_BUILD",
    "GO_RPATH_LINK",
    "GO_RPATH",
    "GOVERSION",
    "GPE_MIRROR",
    "GTK2DISTROFEATURES",
    "GTK3DISTROFEATURES",
    "HOMEPAGE",
    "HOST_AR_KERNEL_ARCH",
    "HOST_ARCH",
    "HOST_AS_ARCH",
    "HOST_CC_ARCH",
    "HOST_CC_KERNEL_ARCH",
    "HOST_CFLAGS",
    "HOST_CXXFLAGS",
    "HOST_EXEEXT",
    "HOST_EXTRACFLAGS",
    "HOST_GO386",
    "HOST_GOARCH",
    "HOST_GOARM",
    "HOST_GOMIPS",
    "HOST_GOOS",
    "HOST_GOTUPLE",
    "HOST_LD_ARCH",
    "HOST_LD_KERNEL_ARCH",
    "HOST_OS",
    "HOST_PREFIX",
    "HOST_SYS",
    "HOST_USER_GID",
    "HOST_USER_UID",
    "HOST_VENDOR",
    "HOSTLDFLAGS",
    "HOSTTOOLS_DIR",
    "HOSTTOOLS_NONFATAL",
    "HOSTTOOLS",
    "IMAGE_BASENAME",
    "IMAGE_CLASSES",
    "IMAGE_CMD_TAR",
    "IMAGE_FEATURES",
    "IMAGE_FSTYPES_DEBUGFS",
    "IMAGE_FSTYPES",
    "IMAGE_GEN_DEBUGFS",
    "IMAGE_INSTALL_COMPLEMENTARY",
    "IMAGE_INSTALL_DEBUGFS",
    "IMAGE_INSTALL",
    "IMAGE_LINGUAS",
    "IMAGE_LINK_NAME",
    "IMAGE_MANIFEST",
    "IMAGE_NAME_SUFFIX",
    "IMAGE_NAME",
    "IMAGE_OVERHEAD_FACTOR",
    "IMAGE_PKGTYPE",
    "IMAGE_POSTPROCESS_COMMAND",
    "IMAGE_PREPROCESS_COMMAND",
    "IMAGE_ROOTFS_ALIGNMENT",
    "IMAGE_ROOTFS_EXTRA_SPACE",
    "IMAGE_ROOTFS_SIZE",
    "IMAGE_ROOTFS",
    "IMAGE_TYPES_MASKED",
    "IMAGE_TYPES",
    "IMAGE_VERSION_SUFFIX",
    "IMGCLASSES",
    "IMGDEPLOYDIR",
    "INC_PR",
    "INHERIT_BLACKLIST",
    "INHERIT_DISTRO",
    "INHERIT",
    "INHIBIT_DEFAULT_DEPS",
    "INHIBIT_SYSROOT_STRIP",
    "INHIBIT_UPDATERCD_BBCLASS",
    "INIT_D_DIR",
    "INIT_MANAGER",
    "INITRAMFS_FSTYPES",
    "INITRAMFS_IMAGE_BUNDLE",
    "INITRAMFS_IMAGE_NAME",
    "INITRAMFS_IMAGE",
    "INITRAMFS_LINK_NAME",
    "INITRAMFS_MAXSIZE",
    "INITRAMFS_NAME",
    "INITRAMFS_TASK",
    "INITSCRIPT_NAME_${PN}",
    "INITSCRIPT_NAME",
    "INITSCRIPT_PACKAGES",
    "INITSCRIPT_PARAMS_${PN}",
    "INITSCRIPT_PARAMS",
    "IPKGCONF_SDK",
    "IPKGCONF_TARGET",
    "JFFS2_ENDIANNESS",
    "JFFS2_ERASEBLOCK",
    "JFFS2_SUM_EXTRA_ARGS",
    "KBRANCH",
    "KBUILD_OUTPUT",
    "KCONF_AUDIT_LEVEL",
    "KCONF_BSP_AUDIT_LEVEL",
    "KCONFIG_CONFIG_COMMAND",
    "KEEPUIMAGE",
    "KERNEL_ALT_IMAGETYPE",
    "KERNEL_AR",
    "KERNEL_ARTIFACT_LINK_NAME",
    "KERNEL_ARTIFACT_NAME",
    "KERNEL_CC",
    "KERNEL_CLASSES",
    "KERNEL_CONFIG_COMMAND",
    "KERNEL_CONSOLE",
    "KERNEL_DEPLOYSUBDIR",
    "KERNEL_DEVICETREE_BUNDLE",
    "KERNEL_DTB_LINK_NAME",
    "KERNEL_DTB_NAME",
    "KERNEL_EXTRA_ARGS",
    "KERNEL_EXTRA_FEATURES",
    "KERNEL_FEATURES",
    "KERNEL_FIT_LINK_NAME",
    "KERNEL_FIT_NAME",
    "KERNEL_IMAGE_LINK_NAME",
    "KERNEL_IMAGE_NAME",
    "KERNEL_IMAGEDEST",
    "KERNEL_IMAGETYPE_FOR_MAKE",
    "KERNEL_IMAGETYPE",
    "KERNEL_IMAGETYPES",
    "KERNEL_LD",
    "KERNEL_LOCALVERSION",
    "KERNEL_MODULE_AUTOLOAD",
    "KERNEL_MODULE_PACKAGE_PREFIX",
    "KERNEL_MODULE_PACKAGE_SUFFIX",
    "KERNEL_MODULE_PROBECONF",
    "KERNEL_MODULE_PROVIDE_VIRTUAL",
    "KERNEL_MODULES_META_PACKAGE",
    "KERNEL_OUTPUT_DIR",
    "KERNEL_PACKAGE_NAME",
    "KERNEL_RELEASE",
    "KERNEL_SRC_PATH",
    "KERNEL_VERSION_NAME",
    "KERNEL_VERSION_PKG_NAME",
    "KERNEL_VERSION",
    "KERNELDEPMODDEPEND",
    "KERNELORG_MIRROR",
    "KMACHINE",
    "KMETA_AUDIT",
    "KMETA",
    "LAYER_CONF_VERSION",
    "LAYERSERIES_CORENAMES",
    "LDCONFIGDEPEND",
    "LDFLAGS",
    "LDLIBS",
    "LIBC_DEPENDENCIES",
    "LIBCEXTENSION",
    "LIBCOVERRIDE",
    "LIBCPLUSPLUS",
    "LIBS",
    "LIC_FILES_CHKSUM",
    "LICENSE_CREATE_PACKAGE",
    "LICENSE_DIRECTORY",
    "LICENSE_FILES_DIRECTORY",
    "LICENSE_PACKAGE_SUFFIX",
    "LICENSE_PATH",
    "LICENSE",
    "LICSSTATEDIR",
    "LINGUAS_INSTALL",
    "LINKER_HASH_STYLE",
    "LINUX_KERNEL_TYPE",
    "LINUX_VERSION_EXTENSION",
    "LINUX_VERSION",
    "LINUXLIBCVERSION",
    "LLVMVERSION",
    "LOCALCONF_VERSION",
    "LOCALE_SECTION",
    "LOCALE_UTF8_IS_DEFAULT",
    "LOCALE_UTF8_ONLY",
    "LOCALEBASEPN",
    "LOG_DIR",
    "LOGFIFO",
    "LUA_TARGET_OS",
    "MACHINE_ARCH",
    "MACHINE_ESSENTIAL_EXTRA_RDEPENDS",
    "MACHINE_ESSENTIAL_EXTRA_RRECOMMENDS",
    "MACHINE_EXTRA_RDEPENDS",
    "MACHINE_EXTRA_RRECOMMENDS",
    "MACHINE_FEATURES_BACKFILL_CONSIDERED",
    "MACHINE_FEATURES_BACKFILL",
    "MACHINE_FEATURES",
    "MACHINE_HWCODECS",
    "MACHINE_TASK_PROVIDER",
    "MACHINEOVERRIDES",
    "MAINTAINER",
    "METADATA_BRANCH",
    "METADATA_REVISION",
    "MIN_BTRFS_SIZE",
    "MIN_F2FS_SIZE",
    "MIRRORS",
    "MLPREFIX",
    "MODULE_TARBALL_DEPLOY",
    "MODULE_TARBALL_LINK_NAME",
    "MODULE_TARBALL_NAME",
    "MULTI_PROVIDER_WHITELIST",
    "MULTILIB_CHECK_FILE",
    "MULTILIB_TEMP_ROOTFS",
    "MULTILIB_VARIANTS",
    "MULTILIBRE_ALLOW_REP",
    "MULTIMACH_TARGET_SYS",
    "NATIVE_PACKAGE_PATH_SUFFIX",
    "NATIVELSBSTRING",
    "NO_RECOMMENDATIONS",
    "NO32LIBS",
    "NPM_ARCH",
    "NPM_EXTRA_ARGS",
    "NPM_LIBDIR",
    "NPM_TAR_FILENAME",
    "OE_DEL",
    "OE_EXTRA_IMPORTS",
    "OE_FEATURES",
    "OE_IMPORTED",
    "OE_IMPORTS",
    "OE_INIT_ENV_SCRIPT",
    "OE_TERMINAL_EXPORTS",
    "OE_TERMINAL",
    "OECMAKE_RPATH",
    "OEINCLUDELOGS",
    "OELAYOUT_ABI",
    "OES_BITBAKE_CONF",
    "OLDEST_KERNEL",
    "OPKG_ARGS",
    "OPKG_POSTPROCESS_COMMANDS",
    "OPKG_PREPROCESS_COMMANDS",
    "OPKGBUILDCMD",
    "OPKGLIBDIR",
    "OVERRIDES",
    "P",
    "PACKAGE_ARCH",
    "PACKAGE_ARCHS",
    "PACKAGE_BEFORE_PN",
    "PACKAGE_CLASSES",
    "PACKAGE_DEBUG_SPLIT_STYLE",
    "PACKAGE_DEPENDS",
    "PACKAGE_EXCLUDE",
    "PACKAGE_EXTRA_ARCHS",
    "PACKAGE_INSTALL_ATTEMPTONLY",
    "PACKAGE_PREPROCESS_FUNCS",
    "PACKAGE_WRITE_DEPS",
    "PACKAGEBUILDPKGD",
    "PACKAGECONFIG_CONFARGS",
    "PACKAGECONFIG_NUMA",
    "PACKAGECONFIG",
    "PACKAGEFUNCS",
    "PACKAGEINDEXDEPS",
    "PACKAGES_DYNAMIC",
    "PACKAGES",
    "PACKAGESPLITFUNCS",
    "PACKAGEVARS",
    "PARALLEL_MAKE",
    "PARALLEL_MAKEINST",
    "PATCH_GIT_USER_EMAIL",
    "PATCH_GIT_USER_NAME",
    "PATCHDEPENDENCY",
    "PATCHRESOLVE",
    "PATCHTOOL",
    "PE",
    "PERSISTENT_DIR",
    "PF",
    "PHP_LIBDIR",
    "PID",
    "PKGD",
    "PKGDATA_DIR",
    "PKGDATA_VARS",
    "PKGDEST",
    "PKGDESTWORK",
    "PKGE",
    "PKGMLTRIPLETS",
    "PKGR",
    "PKGTRIPLETS",
    "PKGV",
    "PKGWRITEDIRIPK",
    "PN",
    "POKY_BBLAYERS_CONF_VERSION",
    "POKY_DEFAULT_DISTRO_FEATURES",
    "POKY_DEFAULT_EXTRA_RDEPENDS",
    "POKY_DEFAULT_EXTRA_RRECOMMENDS",
    "POKYQEMUDEPS",
    "POPULATE_SDK_POST_HOST_COMMAND",
    "POPULATESYSROOTDEPS",
    "POSTINST_INTERCEPT_CHECKSUMS",
    "POSTINST_INTERCEPTS_DIR",
    "POSTINST_INTERCEPTS_PATHS",
    "POSTINST_INTERCEPTS",
    "POSTINST_LOGFILE",
    "PR",
    "PRAUTO",
    "PRAUTOINX",
    "PREMIRRORS",
    "PREPROCESS_RELOCATE_DIRS",
    "PRIORITY",
    "PROVIDES",
    "PSEUDO_LOCALSTATEDIR",
    "PSEUDO_PASSWD",
    "PSEUDO_SYSROOT",
    "PTEST_BINDIR_PKGD_PATH",
    "PTEST_BINDIR",
    "PTEST_BUILD_HOST_FILES",
    "PTEST_BUILD_HOST_PATTERN",
    "PTEST_ENABLED",
    "PTEST_PATH",
    "PV",
    "PYTHON_ABI",
    "PYTHON_BASEVERSION",
    "PYTHON_DIR",
    "PYTHON_PN",
    "PYTHON_SITEPACKAGES_DIR",
    "PYTHON",
    "QA_LOGFILE",
    "QA_SANE",
    "QB_AUDIO_DRV",
    "QB_AUDIO_OPT",
    "QB_CPU_KVM",
    "QB_CPU",
    "QB_DEFAULT_FSTYPE",
    "QB_DEFAULT_KERNEL",
    "QB_DRIVE_TYPE",
    "QB_KERNEL_CMDLINE_APPEND",
    "QB_MEM",
    "QB_NETWORK_DEVICE",
    "QB_OPT_APPEND",
    "QB_SERIAL_OPT",
    "QB_SYSTEM_NAME",
    "QEMU_OPTIONS",
    "QEMUVERSION",
    "QUILTRCFILE",
    "RDEPENDS",
    "REAL_MULTIMACH_TARGET_SYS",
    "RECIPE_MAINTAINER",
    "RECIPE_SYSROOT_NATIVE",
    "RECIPE_SYSROOT",
    "RECIPERDEPTASK",
    "REMOVE_LIBTOOL_LA",
    "REQUIRED_POKY_BBLAYERS_CONF_VERSION",
    "RM_WORK_BUILD_WITHOUT",
    "RM_WORK_EXCLUDE_ITEMS",
    "RM_WORK_EXCLUDE",
    "RMINITDIR",
    "ROOT_HOME",
    "ROOTFS_BOOTSTRAP_INSTALL",
    "ROOTFS_PKGMANAGE",
    "ROOTFS_RO_UNNEEDED",
    "RPMDEPS",
    "RPROVIDES",
    "RRECOMMENDS",
    "RUNNABLE_IMAGE_TYPES",
    "RUNNABLE_MACHINE_PATTERNS",
    "RUNTIME",
    "S",
    "SANITY_ABIFILE",
    "SANITY_BBLAYERCONF_SAMPLE",
    "SANITY_DIFF_TOOL",
    "SANITY_LOCALCONF_SAMPLE",
    "SANITY_REQUIRED_UTILITIES",
    "SANITY_SITECONF_SAMPLE",
    "SANITY_TESTED_DISTROS",
    "SANITY_VERSION",
    "SAVANNAH_GNU_MIRROR",
    "SAVANNAH_NONGNU_MIRROR",
    "SDK_ARCH",
    "SDK_ARCHIVE_CMD",
    "SDK_ARCHIVE_DEPENDS",
    "SDK_ARCHIVE_TYPE",
    "SDK_AS_ARCH",
    "SDK_CC_ARCH",
    "SDK_DEPENDS",
    "SDK_DEPLOY",
    "SDK_DIR",
    "SDK_EXT_HOST_MANIFEST",
    "SDK_EXT_TARGET_MANIFEST",
    "SDK_EXT_TYPE",
    "SDK_EXT",
    "SDK_HOST_MANIFEST",
    "SDK_INCLUDE_NATIVESDK",
    "SDK_INCLUDE_PKGDATA",
    "SDK_INCLUDE_TOOLCHAIN",
    "SDK_INHERIT_BLACKLIST",
    "SDK_INSTALL_TARGETS",
    "SDK_LD_ARCH",
    "SDK_LOCAL_CONF_BLACKLIST",
    "SDK_LOCAL_CONF_WHITELIST",
    "SDK_NAME_PREFIX",
    "SDK_NAME",
    "SDK_OLDEST_KERNEL",
    "SDK_OS",
    "SDK_OUTPUT",
    "SDK_PACKAGE_ARCHS",
    "SDK_PACKAGING_COMMAND",
    "SDK_PACKAGING_FUNC",
    "SDK_POST_INSTALL_COMMAND",
    "SDK_PRE_INSTALL_COMMAND",
    "SDK_PREFIX",
    "SDK_RDEPENDS",
    "SDK_RECRDEP_TASKS",
    "SDK_RELOCATE_AFTER_INSTALL",
    "SDK_SYS",
    "SDK_TARGET_MANIFEST",
    "SDK_TARGETS",
    "SDK_TITLE",
    "SDK_UPDATE_URL",
    "SDK_VENDOR",
    "SDK_VERSION",
    "SDKDEPLOYDIR",
    "SDKEXTDEPLOYDIR",
    "SDKEXTPATH",
    "SDKGCCVERSION",
    "SDKIMAGE_FEATURES",
    "SDKIMAGE_INSTALL_COMPLEMENTARY",
    "SDKIMAGE_LINGUAS",
    "SDKMACHINE",
    "SDKPATH",
    "SDKPATHNATIVE",
    "SDKPKGSUFFIX",
    "SDKTARGETSYSROOT",
    "SDKTAROPTS",
    "SDKUSE_NLS",
    "SECTION",
    "SECURITY_CFLAGS",
    "SECURITY_LDFLAGS",
    "SECURITY_NO_PIE_CFLAGS",
    "SECURITY_NOPIE_CFLAGS",
    "SECURITY_PIE_CFLAGS",
    "SECURITY_STACK_PROTECTOR",
    "SECURITY_STRINGFORMAT",
    "SECURITY_X_LDFLAGS",
    "SELECTED_OPTIMIZATION",
    "SERIAL_CONSOLE",
    "SERIAL_CONSOLES",
    "SHLIBSDIRS",
    "SHLIBSWORKDIR",
    "SIGGEN_EXCLUDE_SAFE_RECIPE_DEPS",
    "SIGGEN_EXCLUDERECIPES_ABISAFE",
    "SIGGEN_LOCKEDSIGS_SSTATE_EXISTS_CHECK",
    "SIGGEN_LOCKEDSIGS_TASKSIG_CHECK",
    "SITE_CONF_VERSION",
    "SITECONFIG_SYSROOTCACHE",
    "SITEINFO_BITS",
    "SITEINFO_ENDIANNESS",
    "SOLIBS",
    "SOLIBSDEV",
    "SORT_PASSWD_POSTPROCESS_COMMAND",
    "SOURCEFORGE_MIRROR",
    "SPDX_MANIFEST_DIR",
    "SPDX_TEMP_DIR",
    "SPDX_VERSION",
    "SPECIAL_PKGSUFFIX",
    "SPLASH",
    "SRC_DISTRIBUTE_LICENSES",
    "SRC_URI",
    "SRCDATE",
    "SRCPV",
    "SRCREV_FORMAT",
    "SRCREV",
    "SRCTREECOVEREDTASKS",
    "SSH_AGENT_PID",
    "SSH_AUTH_SOCK",
    "SSTATE_ARCHS",
    "SSTATE_DIR",
    "SSTATE_DUPWHITELIST",
    "SSTATE_EXCLUDEDEPS_SYSROOT",
    "SSTATE_EXTRAPATH",
    "SSTATE_EXTRAPATHWILDCARD",
    "SSTATE_HASHEQUIV_METHOD",
    "SSTATE_HASHEQUIV_REPORT_TASKDATA",
    "SSTATE_MANFILEPREFIX",
    "SSTATE_MANIFESTS",
    "SSTATE_MANMACH",
    "SSTATE_PATHSPEC",
    "SSTATE_PKG",
    "SSTATE_PKGARCH",
    "SSTATE_PKGNAME",
    "SSTATE_PKGSPEC",
    "SSTATE_PRUNE_OBSOLETEWORKDIR",
    "SSTATE_SCAN_CMD_NATIVE",
    "SSTATE_SCAN_CMD",
    "SSTATE_SCAN_FILES",
    "SSTATE_SIG_KEY",
    "SSTATE_SIG_PASSPHRASE",
    "SSTATE_SWSPEC",
    "SSTATE_VERIFY_SIG",
    "SSTATE_VERSION",
    "SSTATECREATEFUNCS",
    "SSTATEPOSTCREATEFUNCS",
    "SSTATEPOSTINSTFUNCS",
    "SSTATEPOSTUNPACKFUNCS",
    "SSTATEPREINSTFUNCS",
    "SSTATETASKS",
    "STAGING_BASE_LIBDIR_NATIVE",
    "STAGING_BASELIBDIR",
    "STAGING_BINDIR_CROSS",
    "STAGING_BINDIR_NATIVE",
    "STAGING_BINDIR_TOOLCHAIN",
    "STAGING_BINDIR",
    "STAGING_DATADIR_NATIVE",
    "STAGING_DATADIR",
    "STAGING_DIR_HOST",
    "STAGING_DIR_NATIVE",
    "STAGING_DIR_TARGET",
    "STAGING_DIR",
    "STAGING_ETCDIR_NATIVE",
    "STAGING_EXECPREFIXDIR",
    "STAGING_FIRMWARE_DIR",
    "STAGING_INCDIR_NATIVE",
    "STAGING_INCDIR",
    "STAGING_KERNEL_BUILDDIR",
    "STAGING_KERNEL_DIR",
    "STAGING_LIBDIR_NATIVE",
    "STAGING_LIBDIR",
    "STAGING_LIBEXECDIR_NATIVE",
    "STAGING_LIBEXECDIR",
    "STAGING_LOADER_DIR",
    "STAGING_SBINDIR_NATIVE",
    "STAMP",
    "STAMPCLEAN",
    "STAMPS_DIR",
    "SUMMARY",
    "SYSROOT_DESTDIR",
    "SYSROOT_DIR",
    "SYSROOT_DIRS_BLACKLIST",
    "SYSROOT_DIRS_NATIVE",
    "SYSROOT_DIRS",
    "SYSROOT_PREPROCESS_FUNCS",
    "SYSTEMD_AUTO_ENABLE_${PN}",
    "SYSTEMD_AUTO_ENABLE",
    "SYSTEMD_DEFAULT_TARGET",
    "SYSTEMD_PACKAGES",
    "T",
    "TARGET_AR_KERNEL_ARCH",
    "TARGET_AS_ARCH",
    "TARGET_CC_ARCH",
    "TARGET_CC_KERNEL_ARCH",
    "TARGET_CFLAGS",
    "TARGET_CPPFLAGS",
    "TARGET_CXXFLAGS",
    "TARGET_FPU",
    "TARGET_GO386",
    "TARGET_GOARCH",
    "TARGET_GOARM",
    "TARGET_GOMIPS",
    "TARGET_GOOS",
    "TARGET_GOTUPLE",
    "TARGET_LD_ARCH",
    "TARGET_LD_KERNEL_ARCH",
    "TARGET_LDFLAGS",
    "TARGET_LINK_HASH_STYLE",
    "TARGET_OS",
    "TARGET_PREFIX",
    "TARGET_SYS",
    "TARGET_VENDOR",
    "TCLIBC",
    "TCLIBCAPPEND",
    "TCMODE",
    "TERMINFO",
    "THISDIR",
    "TIME",
    "TMPDIR",
    "TOOLCHAIN_HOST_TASK_ATTEMPTONLY",
    "TOOLCHAIN_HOST_TASK",
    "TOOLCHAIN_OPTIONS",
    "TOOLCHAIN_OUTPUTNAME",
    "TOOLCHAIN_SHAR_EXT_TMPL",
    "TOOLCHAIN_SHAR_REL_TMPL",
    "TOOLCHAIN_TARGET_TASK_ATTEMPTONLY",
    "TOOLCHAIN_TARGET_TASK",
    "TOOLCHAIN",
    "TOOLCHAINEXT_OUTPUTNAME",
    "TOPDIR",
    "TRANSLATED_TARGET_ARCH",
    "TUNE_ARCH",
    "TUNE_ASARGS",
    "TUNE_CCARGS",
    "TUNE_FEATURES",
    "TUNE_LDARGS",
    "TUNE_PKGARCH",
    "UBI_VOLNAME",
    "UBOOT_ENTRYPOINT",
    "UBOOT_LOADADDRESS",
    "UBOOT_MACHINE",
    "UNINATIVE_DLDIR",
    "UNINATIVE_LOADER",
    "UNINATIVE_MAXGLIBCVERSION",
    "UNINATIVE_STAGING_DIR",
    "UNINATIVE_TARBALL",
    "UNINATIVE_URL",
    "UNKNOWN_CONFIGURE_WHITELIST",
    "UNWINDLIB",
    "UPDALTVARS",
    "UPDATERCD",
    "UPDATERCPN",
    "UPSTREAM_CHECK_GITTAGREGEX",
    "UPSTREAM_CHECK_REGEX",
    "UPSTREAM_CHECK_URI",
    "USE_DEPMOD",
    "USE_DEVFS",
    "USE_NLS",
    "USER_CLASSES",
    "USING_WIC",
    "USRBINPATH",
    "UVESA_MODE",
    "VOLATILE_LOG_DIR",
    "WARN_QA",
    "WARN_TO_ERROR_QA",
    "WIC_CREATE_EXTRA_ARGS",
    "WICVARS",
    "WKS_FILE_CHECKSUM",
    "WKS_FILE_DEPENDS_BOOTLOADERS",
    "WKS_FILE_DEPENDS_DEFAULT",
    "WKS_FILE_DEPENDS",
    "WKS_FILE",
    "WKS_FILES",
    "WKS_FULL_PATH",
    "WKS_SEARCH_PATH",
    "WORKDIR_PKGDATA",
    "WORKDIR",
    "X86ARCH32",
    "X86ARCH64",
    "XAUTHORITY",
    "XLIBS_MIRROR",
    "XORG_MIRROR",
    "XSERVER",
    "XZ_COMPRESSION_LEVEL",
    "XZ_DEFAULTS",
    "XZ_INTEGRITY_CHECK",
    "ZIP_COMPRESSION_LEVEL"
]
