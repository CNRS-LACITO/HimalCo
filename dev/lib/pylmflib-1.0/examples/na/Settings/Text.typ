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
\mkrOverThis ref
\mkrFollowingThis gn
\-mkr

\+mkr ge
\nam Gloss
\desc English gloss of each morpheme in the morpheme breaks line.
\lng English
\mkrOverThis tx
\-mkr

\+mkr gn
\nam Gloss in national language
\desc Chinese gloss of each morpheme in the morpheme breaks line.
\lng national
\mkrOverThis tx
\mkrFollowingThis nt
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
\lng national
\mkrOverThis ref
\mkrFollowingThis ref
\-mkr

\+mkr ps
\nam Part of Speech
\desc Part of speech of each morpheme in the morpheme breaks line.
\lng English
\mkrOverThis tx
\mkrFollowingThis gn
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
\mkrOverThis ref
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
\File C:\Dropbox\GitHub\HimalCo\dev\lib\pylmflib-1.0\examples\na\Dictionary.txt
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
\File C:\Dropbox\GitHub\HimalCo\dev\lib\pylmflib-1.0\examples\na\Dictionary.txt
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

\+intprc Lookup
\mkrFrom mb
\mkrTo ge

\+triLook 
\dbtyp MDF 4.0
\+drflst 
\+drf 
\File C:\Dropbox\GitHub\HimalCo\dev\lib\pylmflib-1.0\examples\na\Dictionary.txt
\-drf
\-drflst
\+mrflst 
\mkr lx
\-mrflst
\mkrOut ge
\-triLook
\GlossSeparator ;
\FailMark ***
\bShowFailMark
\bShowRootGuess
\-intprc

\+intprc Lookup
\mkrFrom mb
\mkrTo ps

\+triLook 
\dbtyp MDF 4.0
\+drflst 
\+drf 
\File C:\Dropbox\GitHub\HimalCo\dev\lib\pylmflib-1.0\examples\na\Dictionary.txt
\-drf
\-drflst
\+mrflst 
\mkr lx
\-mrflst
\mkrOut ps
\-triLook
\GlossSeparator ;
\FailMark ***
\bShowFailMark
\bShowRootGuess
\-intprc

\+intprc Lookup
\mkrFrom mb
\mkrTo gn

\+triLook 
\+drflst 
\-drflst
\-triLook
\GlossSeparator ;
\FailMark ***
\bShowFailMark
\bShowRootGuess
\-intprc

\-intprclst
\+filset 

\-filset

\+jmpset 
\+jmp Morphemes
\+mkrsubsetIncluded 
\mkr mb
\-mkrsubsetIncluded
\+drflst 
\+drf 
\File C:\Dropbox\GitHub\HimalCo\dev\lib\pylmflib-1.0\examples\na\Dictionary.txt
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
\mkrTextRef ref
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
