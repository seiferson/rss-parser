rss-parser
==========

RSS Parser in python

#Lexic base#
<rss-file> 			::= <rss version="<n>.<n>"><rss-content></rss>
<rss-content> 		::= <rss-channel><rss-content>|<rss-channel>
<rss-channel>		::= <channel><channel-content></channel>
<channel-content> 	::= <title-dec><link-dec><description-dec><items>
<items>				::= <item-dec><items>|<item-dec>
<item-dec>			::= <item><item-content></item>
<item-content>		::= <title-dec><link-dec><description-dec>
<title-dec>			::= <title><content></title>
<link-dec>			::= <link><content></link>
<description-dec>	::= <description><content></description>
<content>			::= any word,number or space/tab/EOL char
<n>					::= numbers from 0 to 9
