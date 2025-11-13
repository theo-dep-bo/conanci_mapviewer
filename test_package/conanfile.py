import os
from conan import ConanFile
from conan.tools.build import cross_building


class mapviewerTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def layout(self):
        self.folders.build = "build"
        self.folders.generators = "build/generators"
    
    def requirements(self):
        self.requires(self.tested_reference_str)

    def test(self):
        if not cross_building(self):
            self.run("mapviewer", env="conanrun")
