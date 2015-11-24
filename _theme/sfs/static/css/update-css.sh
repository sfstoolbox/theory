#!/bin/bash
#
# If you want to make changes on the css theme *ONLY* edit the theme.css file
# and afterwards run this script to update its minified version which will be
# used by the theme
cleancss -o theme-min.css theme.css
