rss-parser
==========

RSS Parser in python

#Lexic base#
<rss_dec>         ::= <left_chevron><rss><attributes><right_chevron><rss_content><left_chevron><rss_closure><right_chevron>
<rss_content>     ::= <channel_dec><rss_content>
<rss_content>     ::= <channel_dec>
<channel_dec>     ::= <left_chevron><channel><attributes><rigth_chevron><channel_content><left_chevron><channel_closure><right_chevron>
<channel_content> ::= <title_dec><link_dec><desc_dec><items>
<items>           ::= <item_dec><items>
<items>           ::= <item_dec>
<item_dec>        ::= <left_chevron><item><attributes><rigth_chevron><item_content><left_chevron><item_closure><right_chevron>
<item_content>    ::= <title_dev><link_dec><desc_dec>
<title_dec>       ::= <left_chevron><title><attributes><right_chevron><content><left_chevron><title_closure><rigth_chevron>
<link_dec>        ::= <left_chevron><link><attributes><right_chevron><content><left_chevron><link_closure><rigth_chevron>
<desc_dec>        ::= <left_chevron><description><attributes><right_chevron><content><left_chevron><desc_closure><rigth_chevron>
<attributes>      ::= <attribute><attributes>
<attributes>      ::= <attribute>
<attribute>       ::= <epsilon>
<attribute>       ::= <strings><equal><quote><strings><quote>
<strings>         ::= <string><strings>
<strings>         ::= <string>
<content>         ::= <string><content>
<content>         ::= <equal><content>
<content>         ::= <string>
<content>         ::= <equal>

