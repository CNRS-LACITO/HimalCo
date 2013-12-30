\+DatabaseType Text
\ver 5.0
\desc Standard interlinear text type.
\+mkrset 
\lngDefault English
\mkrRecord id

\+mkr ft
\nam Free Translation
\desc Free translation of the referenced text unit. This is not used or modified during interlinearization. It is information to clarify the meaning of the text.
\lng English
\mkrOverThis id
\mkrFollowingThis ref
\-mkr

\+mkr ge
\nam Gloss
\desc English gloss of each morpheme in the morpheme breaks line.
\lng English
\mkrOverThis tx
\-mkr

\+mkr id
\nam Text Name
\desc Identifying name for the text in this record.
\lng English
\-mkr

\+mkr mb
\nam Morphemes
\desc Source text unit divided into morphemes.
\lng vernacular
\mkrOverThis tx
\-mkr

\+mkr nt
\nam Notes
\desc Notes on the referenced text unit. Useful for explanation, clarification, questions, etc.
\lng English
\mkrOverThis id
\-mkr

\+mkr ps
\nam Part of Speech
\desc Part of speech of each morpheme in the morpheme breaks line.
\lng English
\mkrOverThis tx
\-mkr

\+mkr ref
\nam Reference
\desc Reference for the following text unit. References are used for word list and concordance, plus other purposes.  A reference usually consists of a short abbreviation of the text name, followed by a dot and a number. Text numbering and renumbering automatically update references in this form.
\lng English
\mkrOverThis id
\mkrFollowingThis tx
\-mkr

\+mkr tx
\nam Text
\desc Source text unit for interlinearization. Usually a sentence or clause. After interlinearization there may be multiple text lines in a referenced text unit.
\lng vernacular
\mkrOverThis id
\mkrFollowingThis ft
\-mkr

\-mkrset

\iInterlinCharWd 8

\+intprclst 
\fglst {
\fglend }
\mbnd +
\mbrks -

\+intprc Lookup
\bParseProc
\mkrFrom tx
\mkrTo mb

\+triLook 
\+drflst 
\-drflst
\-triLook

\+triPref 
\dbtyp MDF 4.0
\+drflst 
\+drf 
\File C:\Users\alan\ToolboxC\DictionaryFactoryFolder\DictionaryFactoryPackage\DictionaryFactory\Dictionary.txt
\-drf
\+drf 
\File C:\Users\alan\ToolboxC\DictionaryFactoryFolder\DictionaryFactoryPackage\DictionaryFactory\NonDictionary.txt
\-drf
\-drflst
\+mrflst 
\mkr lx
\mkr a
\-mrflst
\mkrOut u
\-triPref

\+triRoot 
\dbtyp MDF 4.0
\+drflst 
\+drf 
\File C:\Users\alan\ToolboxC\DictionaryFactoryFolder\DictionaryFactoryPackage\DictionaryFactory\Dictionary.txt
\-drf
\+drf 
\File C:\Users\alan\ToolboxC\DictionaryFactoryFolder\DictionaryFactoryPackage\DictionaryFactory\NonDictionary.txt
\-drf
\-drflst
\+mrflst 
\mkr lx
\mkr a
\-mrflst
\mkrOut u
\-triRoot
\GlossSeparator ;
\FailMark *
\bShowFailMark
\bShowRootGuess
\bPreferSuffix
\+wdfset 
\wdfPrimary Word
\+wdf Word
\+wdplst 
\-wdplst
\-wdf
\lngPatterns Default
\-wdfset
\-intprc

\-intprclst
\+filset 

\-filset

\+jmpset 
\+jmp Text
\+mkrsubsetIncluded 
\mkr tx
\-mkrsubsetIncluded
\+drflst 
\+drf 
\File C:\Users\alan\ToolboxC\DictionaryFactoryFolder\DictionaryFactoryPackage\DictionaryFactory\Dictionary.txt
\mkr lx
\-drf
\-drflst
\-jmp
\-jmpset

\+template 
\fld \ref
\fld \tx
\-template
\mkrRecord id
\+PrintProperties 
\header File: &f, Date: &d
\footer Page &p
\topmargin 1.00 in
\leftmargin 0.25 in
\bottommargin 1.00 in
\rightmargin 0.25 in
\recordsspace 10
\-PrintProperties
\+expset 

\+expRTF Rich Text Format
\InterlinearSpacing 120
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

\+expSF Standard Format
\-expSF

\SkipProperties
\-expset
\+numbering 
\mkrRef ref
\mkrTxt tx
\+subsetTextBreakMarkers 
\+mkrsubsetIncluded 
\mkr tx
\-mkrsubsetIncluded
\-subsetTextBreakMarkers
\-numbering
\-DatabaseType
