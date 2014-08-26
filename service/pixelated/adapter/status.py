#
# Copyright (c) 2014 ThoughtWorks, Inc.
#
# Pixelated is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pixelated is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Pixelated. If not, see <http://www.gnu.org/licenses/>.

class Status:

    LEAP_FLAGS_STATUSES = {
        '\\Seen': 'read',
        '\\Answered': 'replied'
    }

    @classmethod
    def from_flag(cls, flag):
        return Status(cls.LEAP_FLAGS_STATUSES[flag])

    @classmethod
    def from_flags(cls, flags):
        return set(cls.from_flag(flag) for flag in flags if flag in cls.LEAP_FLAGS_STATUSES.keys())

    def __init__(self, name):
        self.name = name
        self.ident = name.__hash__()

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()

    def __repr__(self):
        return self.name
