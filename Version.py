class Version:
    """
    This class compares different versions of programs
    """
    def __init__(self, version):
        self.version = self._change_version(version)

    @staticmethod
    def _replace_stages_of_development(version):
        if 'a' in version and '-' not in version:
            version = version.replace('a', '-alpha')
        elif 'b' in version and '-' not in version:
            version = version.replace('b', '-beta')
        elif 'rc' in version and '-' not in version:
            version = version.replace('rc', '-rc')
        return version

    def _change_version(self, version):
        if 'a' or 'b' or 'rc' in version:
            version = self._replace_stages_of_development(version)
        if '-' in version:
            version = version.replace('-', '.')
        change_version = version.split('.')
        return change_version

    def __eq__(self, other):
        return self.version == other.version

    def __lt__(self, other):
        version_self = self.version[:3]
        stage_self = self.version[3:]
        version_other = other.version[:3]
        stage_other = other.version[3:]
        if version_self == version_other:
            if stage_self == []:
                return False
            elif stage_other == []:
                return True
            else:
                return stage_self < stage_other
        else:
            return version_self < version_other


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    main()

