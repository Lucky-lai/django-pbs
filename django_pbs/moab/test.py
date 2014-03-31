# Copyright 2008-2014 VPAC
#
# This file is part of django-pbs.
#
# django-pbs is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django-pbs is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django-pbs  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/env python

from django_pbs.moab import MoabServer


if __name__ == "__main__":
	s = MoabServer('edda-m.vpac.org')

	print s.mshow()
	print s.showstart(10, 10)

	print s.showstart(50, 20)
	


