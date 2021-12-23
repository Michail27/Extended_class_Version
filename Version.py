from functools import total_ordering


@total_ordering
class Version:
    """
    This class compares different versions of programs
    """
    def __init__(self, version):
        self.version,  self.version_self, self.stage_self = self._change_version(version)

    @staticmethod
    def _replace_stages_of_development(version):
        literals = (('a', '-alpha'), ('b', '-beta'), ('r', '-rc'))
        for s in literals:
            version = version.replace(*s)
        return version

    def _change_version(self, version):
        if '-' not in version:
            version = self._replace_stages_of_development(version)
        if '-' in version:
            version = version.replace('-', '.')
        change_version = version.split('.')
        version_self = list(map(int, change_version[:3]))
        stage_self = change_version[3:]
        return version, version_self, stage_self

    def __eq__(self, other):
        return self.version == other.version

    def __lt__(self, other):

        if self.version_self != other.version_self:
            return self.version_self < other.version_self
        elif self.stage_self == []:
            return False
        elif other.stage_self == []:
            return True
        else:
            return self.stage_self < other.stage_self


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

    print(Version('1.9.0') < Version('1.11'))


