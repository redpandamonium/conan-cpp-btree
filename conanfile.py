from conans import ConanFile, tools
from conans.tools import download, unzip, check_sha256
import os
import shutil

class LibnameConan(ConanFile):
    name = "cpp-btree"
    description = "B-tree implementation by Google"
    topics = ("conan", "cpp-btree", "B-tree", "data structure")
    url = "https://github.com/bincrafters/conan-cpp-btree"
    homepage = "https://code.google.com/p/cpp-btree/"
    license = "Apache-2.0"
    no_copy_source = True

    _source_subfolder = "cpp-btree"

    def source(self):
        zip_name = "cpp-btree-1.0.1.tar.gz"
        download("https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/cpp-btree/cpp-btree-1.0.1.tar.gz", zip_name)
        check_sha256(zip_name, "5653b0f1b7997627a16c402bf1e633ac3e01dff73ff1eaf0ce39935bb0d4e03d")
        unzip(zip_name)
        shutil.move("cpp-btree-1.0.1", "cpp-btree")
        os.unlink(zip_name)

    def package(self):
        self.copy(pattern="COPYING", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*.h", dst="include", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
