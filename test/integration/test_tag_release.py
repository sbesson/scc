#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2012-2013 University of Dundee & Open Microscopy Environment
# All Rights Reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os
import pytest
import subprocess

from yaclifw.framework import Stop, main
from scc.git import TagRelease
from Sandbox import SandboxTest


class TestTagRelease(SandboxTest):

    def setup_method(self, method):

        super(TestTagRelease, self).setup_method(method)
        self.new_version = '5.0.0-beta1'

    def has_new_prefixed_tag(self, repo):

        return repo.has_local_tag(repo.get_tag_prefix() + self.new_version)

    def tag_release(self, *args):
        args = ["tag-release", "--no-ask"] + list(args)
        main(args=args, items=[("tag-release", TagRelease)])

    def testTag(self):
        """Test tagging on repository without submodules"""

        self.tag_release(self.new_version)
        assert self.has_new_prefixed_tag(self.sandbox)

    def testRecursiveTag(self):
        """Test recursive tagging on repository with submodules"""

        self.init_submodules()
        self.tag_release(self.new_version)
        assert self.has_new_prefixed_tag(self.sandbox)
        for submodule in self.sandbox.submodules:
            assert self.has_new_prefixed_tag(submodule)

    def testShallowTag(self):
        """Test shallow tagging on repository with submodules"""

        self.init_submodules()
        self.tag_release("--shallow", self.new_version)
        assert self.has_new_prefixed_tag(self.sandbox)
        for submodule in self.sandbox.submodules:
            assert not self.has_new_prefixed_tag(submodule)

    def testInvalidVersionNumber(self):
        """Test invalid version number"""

        with pytest.raises(Stop):
            self.tag_release('v5.0.0-beta1')

    def testInvalidVersionPreReleaseNumber(self):
        """Test invalid version pre-release number"""

        with pytest.raises(Stop):
            self.tag_release('0.0.0beta1')

    def testExitingTag(self):
        """Test existing tag"""

        # Create local tag and check local existence
        with open(os.devnull, 'w') as dev_null:
            subprocess.Popen(
                ["git", "tag", 'v.' + self.new_version],
                stdout=dev_null, stderr=dev_null).communicate()
        assert self.sandbox.has_local_tag('v.' + self.new_version)

        # Test Stop is thrown by tag-release command
        with pytest.raises(Stop):
            self.tag_release(self.new_version)

    def testInvalidTag(self):
        """Test invalid tag reference name"""

        # Test Stop is thrown by tag-release command
        with pytest.raises(Stop):
            self.tag_release(self.new_version + "..")
