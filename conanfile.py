from conans import ConanFile, tools
import os

class LibnameConan(ConanFile):
    name = "cpp-btree"
    description = "B-tree implementation by Google"
    topics = ("conan", "cpp-btree", "B-tree", "data structure", "header-only")
    url = "https://github.com/bincrafters/conan-cpp-btree"
    homepage = "https://code.google.com/p/cpp-btree/"
    license = "Apache-2.0"
    no_copy_source = True

    _source_subfolder = "btree"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        ex_dir = "cpp-btree-" + self.version
        os.rename(ex_dir, self._source_subfolder)

    def package(self):
        self.copy(pattern="COPYING", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*.h", dst="include/btree", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
