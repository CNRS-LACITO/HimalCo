\+DatabaseType Semdom4
\ver 5.0
\desc Database type for Semdom4 database
\+mkrset 
\lngDefault English
\mkrRecord is

\+mkr cf
\nam Cross-reference
\lng English
\+fnt 
\Name Times New Roman
\Size 12
\charset 00
\rgbColor 255,0,255
\-fnt
\mkrOverThis is
\-mkr

\+mkr dd
\nam Domain Description
\lng English
\+fnt 
\Name Times New Roman
\Size 12
\charset 00
\rgbColor 0,128,0
\-fnt
\mkrOverThis is
\-mkr

\+mkr ddn
\nam Domain Description-National
\lng English
\mkrOverThis is
\-mkr

\+mkr dt
\nam Datestamp
\lng English
\mkrOverThis is
\-mkr

\+mkr ex
\nam Example words
\lng English
\+fnt 
\Name Times New Roman
\Size 12
\charset 00
\rgbColor 0,0,128
\-fnt
\mkrOverThis is
\CharStyle
\-mkr

\+mkr exn
\nam Example words-National
\lng English
\mkrOverThis is
\Hide
\-mkr

\+mkr exv
\nam *
\lng English
\mkrOverThis is
\-mkr

\+mkr gd
\nam Global identifier
\lng English
\mkrOverThis is
\CharStyle
\-mkr

\+mkr is
\nam Index of Semantics
\lng English
\+fnt 
\Name Times New Roman
\Size 14
\Bold
\charset 00
\rgbColor 255,0,0
\-fnt
\-mkr

\+mkr ix
\nam Index down
\desc Right clicking on the number in this field will move to the next level down in the hierarchy. The \ix and \ixu fields are included as a means of quickly navigating up and down the hierarchy of domains.
\lng English
\MustHaveData
\+fnt 
\Name Times New Roman
\Size 12
\Bold
\charset 00
\rgbColor 255,0,255
\-fnt
\NoWordWrap
\mkrOverThis is
\-mkr

\+mkr ixu
\nam Index Up
\desc Right clicking on the number in this field will move to the next level up in the hierarchy. The \ix and \ixu fields are included as a means of quickly navigating up and down the hierarchy of domains.
\lng English
\+fnt 
\Name Times New Roman
\Size 12
\Bold
\charset 00
\rgbColor 255,0,255
\-fnt
\mkrOverThis is
\-mkr

\+mkr qu
\nam Question
\lng English
\+fnt 
\Name Times New Roman
\Size 12
\Bold
\charset 00
\rgbColor 0,0,0
\-fnt
\mkrOverThis is
\mkrFollowingThis ex
\-mkr

\+mkr qun
\nam Question-National
\lng English
\mkrOverThis is
\Hide
\-mkr

\+mkr sc
\nam Semantic Component
\desc This field is used to describe a semantic component or other issue involved in the semantics of the words in the domain.
\lng English
\mkrOverThis is
\-mkr

\+mkr sd
\nam Semantic Domain
\lng English
\+fnt 
\Name Times New Roman
\Size 14
\Bold
\charset 00
\rgbColor 255,0,0
\-fnt
\mkrOverThis is
\-mkr

\+mkr sdn
\nam Semantic Domain-National
\lng English
\mkrOverThis is
\Hide
\-mkr

\+mkr th
\nam Thesaurus
\lng English
\+fnt 
\Name Times New Roman
\Size 11
\charset 00
\rgbColor 128,0,0
\-fnt
\mkrOverThis is
\mkrFollowingThis sd
\-mkr

\+mkr xe
\nam Example sentence-English
\lng English
\+fnt 
\Name Times New Roman
\Size 12
\charset 00
\rgbColor 0,0,128
\-fnt
\mkrOverThis is
\-mkr

\+mkr xen
\nam Example sentence-National
\lng English
\mkrOverThis is
\Hide
\-mkr

\-mkrset

\iInterlinCharWd 8
\+filset 

\+fil Non-Unique
\fel NonUnique
\match_char c
\-fil

\+fil Unique
\fel Not
\fel NonUnique
\match_char c
\-fil

\+fil XE
\mkr xe
\txt [!]
\match_char c
\-fil

\-filset

\+jmpset 
\+jmp Cross Reference Index
\+mkrsubsetIncluded 
\mkr ix
\mkr ixu
\-mkrsubsetIncluded
\+drflst 
\-drflst
\-jmp
\+jmp cf to sd
\+mkrsubsetIncluded 
\mkr cf
\-mkrsubsetIncluded
\+drflst 
\-drflst
\match_char p
\-jmp
\-jmpset

\+template 
\-template
\mkrRecord is
\mkrDateStamp dt
\+PrintProperties 
\header File: &f, Date: &d
\footer Page &p
\topmargin .50 in
\leftmargin 0.25 in
\bottommargin .5 in
\rightmargin 0.25 in
\printcurrentrecord
\recordsspace 100
\-PrintProperties
\+expset 

\+expRTF Rich Text Format
\exportedFile C:\My Documents\semdom.rtf
\+rtfPageSetup 
\paperSize letter
\topMargin 1
\bottomMargin 1
\leftMargin 1.25
\rightMargin 1.25
\gutter 0
\headerToEdge 0.5
\footerToEdge 0.5
\columns 1
\columnSpacing 0.5
\-rtfPageSetup
\-expRTF

\+expSF SemDom for printing
\PriKeyFieldFirst
\exportedFile C:\Shoedata\Semdom\sd0201.doc
\+mkrsubsetIncluded 
\mkr cf
\mkr dd
\mkr ex
\mkr is
\mkr qu
\-mkrsubsetIncluded
\-expSF

\+expSF Standard Format
\PriKeyFieldFirst
\exportedFile D:\Shoedata\SemDom4\sd4.db
\+mkrsubsetIncluded 
\mkr cf
\mkr dd
\mkr ex
\mkr is
\mkr ix
\mkr ixu
\mkr qu
\mkr sd
\mkr xe
\-mkrsubsetIncluded
\-expSF

\+expSF sf key is
\PriKeyFieldFirst
\exportedFile C:\Language\_Bantu\BI\DDP\Semdom is.db
\+mkrsubsetIncluded 
\mkr cf
\mkr dd
\mkr dt
\mkr ex
\mkr is
\mkr ix
\mkr qu
\mkr sc
\mkr sd
\mkr th
\mkr xe
\-mkrsubsetIncluded
\-expSF

\expDefault Standard Format
\CurrentWindow
\SkipProperties
\-expset
\PreventNumbering
\DisableNumbering
\-DatabaseType
