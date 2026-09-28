%*****************************
% jalc.cls -- document class file
% Created by Bianca Truthe, Feb 28, 2016
% Based on the dcfs07 class file created by Viliam Geffert, Dec 14, 2006
% and on the jalc style file created by Bernd Reichel, Apr 1, 2003
%      Files coming with this distribution:
%      jalc.cls    -- document class itself [this file]
%      jalc-ex.tex -- a sample input with embedded %-comments
%      jalc-ex.bib -- a sample bib-file
%
\NeedsTeXFormat{LaTeX2e}%
\ProvidesClass{jalc}[2018/03/28 jalc]%
%
%!!Options supported by jalc class:
%  "draft" -- version under construction -- default
%  "sub"   -- version to be submitted
%  "rev"   -- revised version
%  "acc"   -- accepted version
%  "proof" -- version for proof reading -- for editor only
%  "fin"   -- final version for publication -- for editor only
%  "pre"   -- final version of preface or editorial -- for editor only
\newcommand*{\bt@opterr}{%--error: "error in submission options"
  \ClassError{jalc}{Multiple submission options are not allowed in jalc style,
    please select only one}%
  {see documentation of the jalc class, file `jalc-ex.pdf'}%
}

\newcommand*{\d@bannr}{%
  \noindent\begin{minipage}{\linewidth}%
    {\footnotesize For submission to the Journal of Automata, Languages and Combinatorics\\[-0.7ex]%
     Created on \today}%
  \end{minipage}}%
\newcommand{\d@phantom}[1]{\mbox{{#1}}}%
\newcommand{\d@markboth}[2]{\markboth{#1}{#2}}%
% To fix incompatability between lineno and amsmath packages:
  \newcommand*\patchAmsMathEnvironmentForLineno[1]{%
    \expandafter\let\csname old#1\expandafter\endcsname\csname #1\endcsname
    \expandafter\let\csname oldend#1\expandafter\endcsname\csname end#1\endcsname
    \renewenvironment{#1}%
       {\linenomath\csname old#1\endcsname}%
       {\csname oldend#1\endcsname\endlinenomath}}% 
  \newcommand*\patchBothAmsMathEnvironmentsForLineno[1]{%
    \patchAmsMathEnvironmentForLineno{#1}%
    \patchAmsMathEnvironmentForLineno{#1*}}%
\newcommand{\ifnotfinalincludelinenumbers}{%
  \usepackage{lineno}\linenumbers%
  \AtBeginDocument{%
  \patchBothAmsMathEnvironmentsForLineno{equation}%
  \patchBothAmsMathEnvironmentsForLineno{align}%
  \patchBothAmsMathEnvironmentsForLineno{flalign}%
  \patchBothAmsMathEnvironmentsForLineno{alignat}%
  \patchBothAmsMathEnvironmentsForLineno{gather}%
  \patchBothAmsMathEnvironmentsForLineno{multline}%
  }%
}%

\DeclareOption{draft}{%
  \@ifundefined{bt@optset}%
  {\newcommand*{\bt@optset}{}%
  }%
  {\bt@opterr}%
}
\DeclareOption{sub}{%
  \@ifundefined{bt@optset}%
  {\newcommand*{\bt@optset}{}\newcommand*{\bt@optsub}{}%
   \renewcommand*{\d@bannr}{%
     \noindent\begin{minipage}{\linewidth}%
       {\footnotesize Submission to the Journal of Automata, Languages and Combinatorics\\[-0.7ex]%
        Submitted on \today}%
     \end{minipage}}%
   %!! uncomment the following if reviewing is double blind (hide authors' identity):
   %\renewcommand{\d@phantom}[1]{\mbox{\phantom{#1}}}%
   %\renewcommand{\d@markboth}[2]{\markboth{#2}{#2}}%
  }%
  {\bt@opterr}%
}
\DeclareOption{rev}{%
  \@ifundefined{bt@optset}%
  {\newcommand*{\bt@optset}{}%
   \renewcommand*{\d@bannr}{%
     \noindent\begin{minipage}{\linewidth}%
       {\footnotesize Revised submission to the Journal of Automata, Languages and Combinatorics\\[-0.7ex]%
        Revised on \today}%
     \end{minipage}}%
  }%
  {\bt@opterr}%
}
\DeclareOption{acc}{%
  \@ifundefined{bt@optset}%
  {\newcommand*{\bt@optset}{}%
   \renewcommand*{\d@bannr}{%
     \noindent\begin{minipage}{\linewidth}%
       {\footnotesize Accepted for publication in the Journal of Automata, Languages and Combinatorics\\[-0.7ex]%
        Final version created on \today}%
     \end{minipage}}%
   \renewcommand{\ifnotfinalincludelinenumbers}{}%
  }%
  {\bt@opterr}%
}
\DeclareOption{proof}{%
  \@ifundefined{bt@optset}%
  {\newcommand*{\bt@optset}{}%
   \renewcommand*{\d@bannr}{%
     \noindent\begin{minipage}{\linewidth}%
       {\footnotesize Accepted for publication in the Journal of Automata, Languages and Combinatorics\\[-0.7ex]%
        Final version created on \today}%
     \end{minipage}}%
   \renewcommand{\ifnotfinalincludelinenumbers}{}%
   \AtEndOfClass{%
     \IfFileExists{proof.clo}%
     {\input{proof.clo}}%
     {\ClassError{jalc}{The option "proof" is only for the editor; 
         if you are the editor, make sure that the file proof.clo is found!}%
         {Make the file proof.clo available or use another class option, e. g., "acc"!}%
      \newcommand*{\jalcVolume}[1]{}%
      \newcommand*{\jalcYear}[1]{}%
      \newcommand*{\jalcNumber}[1]{}%
      \newcommand*{\jalcPageBeg}[1]{}%
      \newcommand*{\jalcPageEnd}[1]{}%
      \newcommand*{\jalcRec}[1]{}%
      \newcommand*{\jalcRev}[1]{}%
     }%
   }%
  }%
  {\bt@opterr}%
}
\DeclareOption{fin}{%
  \@ifundefined{bt@optset}%
  {\newcommand*{\bt@optset}{}%
   \renewcommand*{\d@bannr}{%
     \noindent\begin{minipage}{\linewidth}%
       {\footnotesize Accepted for publication in the Journal of Automata, Languages and Combinatorics\\[-0.7ex]%
        Final version created on \today}%
     \end{minipage}}%
   \renewcommand{\ifnotfinalincludelinenumbers}{}%
   \AtEndOfClass{%
     \IfFileExists{fin.clo}%
     {\input{fin.clo}}%
     {\ClassError{jalc}{The option "fin" is only for the editor; 
         if you are the editor, make sure that the file fin.clo is found!}%
         {Make the file fin.clo available or use another class option, e. g., "acc"!}%
      \newcommand*{\jalcVolume}[1]{}%
      \newcommand*{\jalcYear}[1]{}%
      \newcommand*{\jalcNumber}[1]{}%
      \newcommand*{\jalcPageBeg}[1]{}%
      \newcommand*{\jalcPageEnd}[1]{}%
      \newcommand*{\jalcRec}[1]{}%
      \newcommand*{\jalcRev}[1]{}%
     }%
   }%
  }%
  {\bt@opterr}%
}
\DeclareOption{pre}{%
  \@ifundefined{bt@optset}%
  {\newcommand*{\bt@optset}{}%
   \renewcommand*{\d@bannr}{%
     \noindent\begin{minipage}{\linewidth}%
       {\footnotesize Accepted for publication in the Journal of Automata, Languages and Combinatorics\\[-0.7ex]%
        Final version created on \today}%
     \end{minipage}}%
   \renewcommand{\ifnotfinalincludelinenumbers}{}%
   \AtEndOfClass{%
     \IfFileExists{pre.clo}%
     {\input{pre.clo}}%
     {\ClassError{jalc}{The option "pre" is only for the editor; 
         if you are the editor, make sure that the file pre.clo is found!}%
         {Make the file pre.clo available or use another class option, e. g., "acc"!}%
      \newcommand*{\jalcVolume}[1]{}%
      \newcommand*{\jalcYear}[1]{}%
      \newcommand*{\jalcNumber}[1]{}%
      \newcommand*{\jalcPageBeg}[1]{}%
      \newcommand*{\jalcPageEnd}[1]{}%
      \newcommand*{\jalcRec}[1]{}%
      \newcommand*{\jalcRev}[1]{}%
     }%
   }%
  }%
  {\bt@opterr}%
}
%
%!!The following `article' class options should not be used,
%  so they will be ignored, for compatibility reasons:
\DeclareOption{10pt}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `10pt' ignored (default)}}}
\DeclareOption{11pt}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `11pt' ignored (default 10pt)}}}
\DeclareOption{12pt}{\AtEndOfClass{\ClassWarning{}%
  {Option `12pt' ignored (default 10pt)}}}
\DeclareOption{openlib}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `openlib' ignored}}}
\DeclareOption{leqno}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `leqno' ignored}}}
\DeclareOption{fleqn}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `fleqn' ignored (default)}}}
\DeclareOption{titlepage}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `titlepage' ignored}}}
\DeclareOption{twocolumn}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `twocolumn' ignored}}}
\DeclareOption{a4paper}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `a4paper' ignored (default)}}}
\DeclareOption{letterpaper}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `letterpaper' ignored (default a4paper)}}}
\DeclareOption{a5paper}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `a5paper' ignored (default a4paper)}}}
\DeclareOption{b5paper}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `b5paper' ignored (default a4paper)}}}
\DeclareOption{executivepaper}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `executivepaper' ignored (default a4paper)}}}
\DeclareOption{legalpaper}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `legalpaper' ignored (default a4paper)}}}
\DeclareOption{twoside}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `twoside' ignored (default)}}}
\DeclareOption{oneside}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `oneside' ignored (default twoside)}}}
\DeclareOption{landscape}{\AtEndOfClass{\ClassWarning{jalc}%
  {Option `landscape' ignored}}}
%
%!!Remaining options passed to `article' class:
\DeclareOption*{\PassOptionToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[twoside,10pt,fleqn,a4paper]{article}%
%
\RequirePackage{mathrsfs}
\RequirePackage{xspace}
\PassOptionsToPackage{fleqn}{amsmath}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{tikz}
%\usepackage[ansinew]{inputenc} % for Windows
\usepackage[utf8]{inputenc} % for New UNIX/Linux
%\usepackage[latin1]{inputenc}  % for Unix/Linux
%\usepackage[applemac]{inputenc}% for Apple
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{slantsc}
\usepackage[overload]{textcase}
\usepackage{xcolor}
\usepackage{graphicx}
\ifnotfinalincludelinenumbers
\definecolor{lightgrey}{rgb}{0.67,0.67,0.67}
\newcommand{\eoe}{\hspace*{\fill} \textcolor{lightgrey}{$\blacksquare$}} % end of example
\newcommand{\eor}{\hspace*{\fill} $\diamondsuit$} %end of remark
%\usepackage{ifpdf}
%\ifpdf
\usepackage{etoolbox}
\usetikzlibrary{svg.path}
\definecolor{orcidlogocol}{HTML}{A6CE39}
\tikzset{
  orcidlogo/.pic={
    \fill[orcidlogocol] svg{M256,128c0,70.7-57.3,128-128,128C57.3,256,0,198.7,0,128C0,57.3,57.3,0,128,0C198.7,0,256,57.3,256,128z};
    \fill[white] svg{M86.3,186.2H70.9V79.1h15.4v48.4V186.2z}
                 svg{M108.9,79.1h41.6c39.6,0,57,28.3,57,53.6c0,27.5-21.5,53.6-56.8,53.6h-41.8V79.1z M124.3,172.4h24.5c34.9,0,42.9-26.5,42.9-39.7c0-21.5-13.7-39.7-43.7-39.7h-23.7V172.4z}
                 svg{M88.7,56.8c0,5.5-4.5,10.1-10.1,10.1c-5.6,0-10.1-4.6-10.1-10.1c0-5.6,4.5-10.1,10.1-10.1C84.2,46.7,88.7,51.3,88.7,56.8z};
}}
\AtEndPreamble{\usepackage[bookmarks,bookmarksnumbered,naturalnames,plainpages=false,unicode,urlbordercolor={white}]{hyperref}}
%\else
%\usepackage[dvipdfm,bookmarks,bookmarksnumbered,naturalnames,plainpages=false]{hyperref}
%\fi
\newcommand{\elqq}{`}
\newcommand{\erqq}{'\xspace}
\newcommand{\bteg}{e.\,g.\xspace}
\newcommand{\btie}{i.\,e.\xspace}
\newcommand{\btwrt}{w.\,r.\,t.\xspace}
\newcommand{\btwlog}{w.\,l.\,o.\,g.\xspace}
\newcommand{\qmand}{\quad\mbox{and}\quad}
\newcommand{\mand}{\mbox{ and }}
\newcommand{\dollar}{\$\xspace}
%

%*****************************
%!!Style formatting parameters
%
\setlength{\textheight}{19cm}
\setlength{\textwidth}{13cm}
\setlength{\topmargin}{21mm}
\setlength{\headheight}{10pt}
\setlength{\headsep}{6.7mm}
\setlength{\oddsidemargin}{1.45cm}
\setlength{\evensidemargin}{1.45cm}
\flushbottom
\setlength{\parskip}{0pt\@plus1.3pt}

\setlength{\footnotesep}{9.0pt}
\setlength{\arraycolsep}{0.15em}
%\setlength{\tabcolsep}{0.15em}
\setlength{\doublerulesep}{1.7pt}

\setlength{\intextsep}{10pt\@plus2pt\@minus2pt}
\setlength{\textfloatsep}{11pt\@plus2pt\@minus2pt}
\setlength{\floatsep}{9pt\@plus2pt\@minus2pt}
\renewcommand{\floatpagefraction}{.5}
\mathindent25pt
\parindent12pt
\sloppy
\renewcommand{\arraystretch}{1.2} 
\renewcommand{\topfraction}{0.9999}
\renewcommand{\textfraction}{0.0001}
\renewcommand{\bottomfraction}{0.9999}


%%!!modified clone
%\renewcommand\normalsize{%
%   \@setfontsize\normalsize\@xipt{13.6}%
%   \abovedisplayskip 9\p@\@plus2\p@\@minus4\p@
%   \abovedisplayshortskip \z@\@plus2\p@\@minus1\p@
%   \belowdisplayshortskip 6.5\p@\@plus2\p@\@minus3\p@
%   \belowdisplayskip \abovedisplayskip
%   \let\@listi\@listI}
%\normalsize
%
%%!!modified clone
%\renewcommand\small{%
%   \@setfontsize\small\@xpt\@xiipt
%   \abovedisplayskip 8\p@\@plus1.8\p@\@minus3\p@
%   \abovedisplayshortskip \z@\@plus1.8\p@\@minus0.8\p@
%   \belowdisplayshortskip 6\p@\@plus2\p@\@minus3\p@
%   \def\@listi{\@listI}%
%   \belowdisplayskip \abovedisplayskip
%}

%*****************************
%!!Reductions from the standard article (see also \maketitle)
%
\renewcommand*{\tableofcontents}{}
\renewcommand*{\listoffigures}{}
\renewcommand*{\listoftables}{}
\renewcommand*{\makeindex}{}
\renewcommand*{\makeglossary}{}
\pagenumbering{arabic}%
\renewcommand*{\pagenumbering}[1]{\ignorespaces}
\renewcommand*{\reversemarginpar}{}
\renewcommand*{\normalmarginpar}{}
\renewcommand*{\twocolumn}{\d@err}
\renewcommand*{\part}{\d@err}
\renewcommand*{\date}[1]{\ignorespaces}\let\@date\relax
\renewcommand*{\and}{\d@err}
\renewcommand*{\marginpar}{\d@err}

%*****************************
%!!Modified clones for sectioning and bibliography
%
\renewcommand{\section}{\@startsection{section}{1}{\z@}%
{-3.5ex\@plus-1ex\@minus-0.2ex}{2.3ex\@plus.2ex}{\normalfont\normalsize\bfseries}}
\renewcommand{\subsection}{\@startsection{subsection}{2}{\z@}%
{-3.25ex\@plus-1ex\@minus-0.2ex}{1.5ex\@plus.2ex}{\normalfont\normalsize\itshape}}
\renewcommand{\subsubsection}{\@startsection{subsubsection}{3}{\z@}%
{-3.25ex\@plus-1ex\@minus-0.2ex}{1.5ex\@plus.2ex}{\normalfont\normalsize\itshape}}
\renewcommand{\paragraph}{\@startsection{paragraph}{4}{\z@}%
{2.25ex\@plus1.1ex\@minus0.2ex}{-0.5em}{\normalfont\normalsize\itshape}}
\renewcommand{\subparagraph}{\@startsection{subparagraph}{4}%
  {\parindent}{2.25ex\@plus1.1ex%
  \@minus0.2ex}{-0.5em}{\normalfont\normalsize\itshape}}
\def\@sect#1#2#3#4#5#6[#7]#8{\ifnum #2>\c@secnumdepth
     \let\@svsec\@empty\else
     \refstepcounter{#1}\edef\@svsec{\csname the#1\endcsname.\hskip 0.5em}\fi
     \@tempskipa #5\relax
      \ifdim \@tempskipa>\z@
        \begingroup #6\relax
          \@hangfrom{\hskip #3\relax\@svsec}{\interlinepenalty \@M #8\par}%
        \endgroup
       \csname #1mark\endcsname{#7}\addcontentsline
         {toc}{#1}{\ifnum #2>\c@secnumdepth \else
                      \protect\numberline{\csname the#1\endcsname}\fi
                    #7}\else
        \def\@svsechd{#6\hskip #3\relax  
                   \@svsec #8\csname #1mark\endcsname
                      {#7}\addcontentsline
                           {toc}{#1}{\ifnum #2>\c@secnumdepth \else
                             \protect\numberline{\csname the#1\endcsname}\fi
                       #7}}\fi
     \@xsect{#5}}


\renewcommand*{\newblock}{\hskip .11em\@plus.11em\@minus.07em}
\renewcommand{\thebibliography}[1]{\section*{\refname}\small
  \list{\@biblabel{\arabic{enumiv}}}{%
    \settowidth{\labelwidth}{\@biblabel{#1}}%
    \setlength{\leftmargin}{\labelwidth}%
      \addtolength{\leftmargin}{\labelsep}%
    \setlength{\parsep}{0ex\@plus0.2ex\@minus0.04ex}%
    \setlength{\itemsep}{0.9ex}%
    \usecounter{enumiv}\let\p@enumiv\@empty%
    \renewcommand\theenumiv{\arabic{enumiv}}%
  }%
  \sloppy \clubpenalty4000%
  \@clubpenalty\clubpenalty \widowpenalty4000%
  \sfcode`\.\@m}%
\renewcommand{\endthebibliography}{\renewcommand{\@noitemerr}{\@warning{Empty
  `thebibliography' environment}}%
\endlist}

%*****************************
%!!Modified clones for lists and captions
%
\renewcommand{\@makecaption}[2]{%
  \vskip 5pt%
  \@tempdima\hsize \advance\@tempdima-8mm%!!=2\parindent%
  \setbox\@tempboxa\hbox{{\normalfont\small#1:\ #2}}%
  \ifdim\wd\@tempboxa<\hsize%
    \hfil{\normalfont\small#1:\ #2}\hfil%
  \else
%    \setbox\@tempboxa\hbox{{\normalfont\small#1:\ }}%
%    \advance\@tempdima-\wd\@tempboxa%
%    \hbox to\hsize{\hfil{\normalfont\small{#1:}}\ \parbox[t]\@tempdima{\normalfont\small #2}\hfil}%
    \hfil\parbox\@tempdima{\normalfont\small#1:\ #2}\hfil%
  \fi%
  \vskip 5pt%
}

\addtolength{\labelwidth}{25pt}\addtolength{\itemindent}{25pt}
\renewcommand*{\labelenumi}{{\rm (}\theenumi{\rm )}}
\renewcommand*{\theenumi}{$\scriptstyle\mathrm{\Roman{enumi}}$}

\renewcommand*{\labelenumii}{{\rm (}\theenumii{\rm )}}
\renewcommand*{\theenumii}{$\scriptstyle\mathrm{\Alph{enumii}}$}
\renewcommand*{\p@enumii}{\theenumi.}

\renewcommand*{\labelenumiii}{{\rm (}\theenumiii{\rm )}}
\renewcommand*{\theenumiii}{$\scriptstyle\mathrm{\arabic{enumiii}}$}
\renewcommand*{\p@enumiii}{\p@enumii\theenumii.}

\renewcommand*{\labelenumiv}{{\rm (}\theenumiv{\rm )}}
\renewcommand*{\theenumiv}{$\scriptstyle\mathrm{\alph{enumiv}}$}
\renewcommand*{\p@enumiv}{\p@enumiii\theenumiii.}

\renewcommand*{\labelitemi}{$\bullet$}
\renewcommand*{\labelitemii}{$\ast$}
\renewcommand*{\labelitemiii}{$\circ$}
\renewcommand*{\labelitemiv}{$\scriptstyle\diamond$}

\renewcommand{\descriptionlabel}[1]{\setbox\@tempboxa\hbox{#1}%
  \ifdim\wd\@tempboxa<\labelwidth \makebox[\labelwidth][l]{#1}%
    \else {#1}\fi
}
\renewcommand*{\makelabel}{}
\renewcommand{\description}{%
\list{}{\let\makelabel\descriptionlabel}}%
\renewcommand{\enddescription}{\endlist}

%\setlength{\leftmargini}{2\parindent}
%\setlength{\leftmarginii}{\parindent}
%\setlength{\leftmarginiii}{\parindent}
%\setlength{\leftmarginiv}{\parindent}
%\setlength{\leftmarginv}{\parindent}
%\setlength{\leftmarginvi}{\parindent}

%\setlength{\leftmargin}{\leftmargini}
\setlength{\labelsep}{.5em}
\setlength{\labelwidth}{\leftmargini}
  \addtolength{\labelwidth}{-\labelsep}

\renewcommand{\@listI}{\setlength{\leftmargin}{\leftmargini}%
  \setlength{\rightmargin}{0pt}%
  \setlength{\labelsep}{0.75em}%
  \setlength{\labelwidth}{\leftmargin}%
    \addtolength{\labelwidth}{-\labelsep}%
  \setlength{\listparindent}{\parindent}%
  \setlength{\itemindent}{0em}%
  \setlength{\partopsep}{0.6\baselineskip\@plus0.3ex\@minus0.1ex}%
  \setlength{\topsep}{0.4ex}%
  \setlength{\itemsep}{0.4ex}%
  \setlength{\parsep}{0ex\@plus1.3pt}%
}

\let\@listi\@listI
\@listi

\renewcommand{\@listii}{\setlength{\leftmargin}{\leftmarginii}%
  \setlength{\rightmargin}{0pt}%
  \setlength{\labelsep}{0.75em}%
  \setlength{\labelwidth}{\leftmargin}%
    \addtolength{\labelwidth}{-\labelsep}%
  \setlength{\listparindent}{\parindent}%
  \setlength{\itemindent}{0em}%
  \setlength{\partopsep}{0.5\baselineskip\@plus0.2ex\@minus0.1ex}%
  \setlength{\topsep}{0.3ex}%
  \setlength{\itemsep}{0.3ex}%
  \setlength{\parsep}{0ex\@plus1.3pt}%
}

\renewcommand{\@listiii}{\setlength{\leftmargin}{\leftmarginiii}%
  \setlength{\labelwidth}{\leftmargin}%
    \addtolength{\labelwidth}{-\labelsep}}

\renewcommand{\@listiv}{\setlength{\leftmargin}{\leftmarginiv}%
  \setlength{\labelwidth}{\leftmargin}%
    \addtolength{\labelwidth}{-\labelsep}}

\renewcommand{\@listv}{\setlength{\leftmargin}{\leftmarginv}%
  \setlength{\labelwidth}{\leftmargin}%
    \addtolength{\labelwidth}{-\labelsep}}

\renewcommand{\@listvi}{\setlength{\leftmargin}{\leftmarginvi}%
  \setlength{\labelwidth}{\leftmargin}%
    \addtolength{\labelwidth}{-\labelsep}}

%*****************************
%!!Built-in theorem-like environments
%
\newcounter{claim}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{problem}[theorem]{Problem}
\newtheorem{definition}[theorem]{Definition\dromanb}
\newtheorem{claim}[theorem]{\itshape Claim\d@cproof}
\newcommand*{\dromanb}{\gdef\d@tstyle{\rmfamily\upshape\mdseries}}
\newtheorem{remark*}[theorem]{Remark\dromanb}
\newtheorem{example*}[theorem]{Example\dromanb}

\newcommand{\newmarkedremark}[1]{%
  \newenvironment{#1}
    {\csname inner@#1\endcsname}
    {\eor\csname endinner@#1\endcsname}%
  \newtheorem{inner@#1}%
}
\newmarkedremark{remark}[theorem]{Remark\dromanb}
\newcommand{\newmarkedexample}[1]{%
  \newenvironment{#1}
    {\csname inner@#1\endcsname}
    {\eoe\csname endinner@#1\endcsname}%
  \newtheorem{inner@#1}%
}
\newmarkedexample{example}[theorem]{Example\dromanb}


\newcommand{\d@tstyle}{}
\renewcommand{\@begintheorem}[2]{%
  \par\gdef\d@tstyle{\rmfamily\itshape\mdseries}\trivlist
  \item[\hskip\labelsep{\rmfamily\upshape\bfseries
    #1\ #2.}]\d@tstyle\ignorespaces}
\renewcommand{\@opargbegintheorem}[3]{%
  \par\gdef\d@tstyle{\rmfamily\itshape\mdseries}\trivlist
  \item[\hskip\labelsep{\rmfamily\upshape\bfseries
    #1\ #2\hskip\labelsep #3.}]\d@tstyle\ignorespaces}
\newcounter{d@proof}\let\thed@proof\relax\setcounter{d@proof}{0}
\newcommand*{\d@cproof}{%
  \ifnum \value{d@proof}=0{\@warning{\protect\begin{claim} ...
    \protect\end{claim} not nested in any `proof'^^J or `proofof'
    environment,}}\else\fi
}

%\newcommand*{\qed}{\raisebox{0.5ex}[0ex][0ex]{\framebox[1ex][l]{}}}
\newcommand*{\qed}{\hspace*{\fill}$\Box$}

%\newenvironment{proof}{%
%  \ifnum \value{d@proof}=0{\setcounter{claim}{0}}\else\fi
%  \stepcounter{d@proof}\par\noindent
%  {\rmfamily\itshape\mdseries Proof.}\hspace{\labelsep}\ignorespaces}%
%  {\addtocounter{d@proof}{-1}\mbox{}\nolinebreak\hfill~%
%  \ifnum \value{d@proof}=0{\qed}\else
%    \ifnum \value{d@proof}=1{\qed\nolinebreak\,\nolinebreak\qed}\else
%      \ifnum \value{d@proof}=2{\qed\nolinebreak\,\nolinebreak\qed
%          \nolinebreak\,\nolinebreak\qed}\else
%        {\qed\nolinebreak...\nolinebreak\qed}%
%  \fi\fi\fi
%  \medbreak
%}
\newenvironment{proof}{%
  \ifnum \value{d@proof}=0{\setcounter{claim}{0}}\else\fi
  \stepcounter{d@proof}\par\noindent
  {\rmfamily\itshape\mdseries Proof.}\hspace{\labelsep}\ignorespaces}%
  {\addtocounter{d@proof}{-1}\mbox{}\nolinebreak\hfill~%
  \ifnum \value{d@proof}=0{\qed}\else
    \ifnum \value{d@proof}=1{\hbox{\qed\nolinebreak\,\nolinebreak\qed}}\else
      \ifnum \value{d@proof}=2{\hbox{\qed\nolinebreak\,\nolinebreak\qed\nolinebreak\,\nolinebreak\qed}}\else
        {\hbox{\qed\nolinebreak...\nolinebreak\qed}}%
  \fi\fi\fi
  \medbreak
}

\newenvironment{proof*}{%
  \ifnum \value{d@proof}=0{\setcounter{claim}{0}}\else\fi
  \stepcounter{d@proof}\par\noindent
  {\rmfamily\itshape\mdseries Proof.}\hspace{\labelsep}\ignorespaces}%
  {\addtocounter{d@proof}{-1}%
  \ifnum \value{d@proof}=0{}\else\mbox{}\nolinebreak\hfill~%
    \ifnum \value{d@proof}=1{\hbox{\qed\nolinebreak\,\nolinebreak\qed}}\else
      \ifnum \value{d@proof}=2{\hbox{\qed\nolinebreak\,\nolinebreak\qed\nolinebreak\,\nolinebreak\qed}}\else
        {\hbox{\qed\nolinebreak...\nolinebreak\qed}}%
  \fi\fi\fi
  \medbreak
}

\newenvironment{proofof}[1]{%
  \vspace{\parskip}\vspace{\topsep}\vspace{\partopsep}%
  \ifnum \value{d@proof}=0{\setcounter{claim}{0}}\else\fi
  \stepcounter{d@proof}\par\noindent
  {\rmfamily\itshape\mdseries Proof of #1.}\hspace{\labelsep}\ignorespaces}%
  {\addtocounter{d@proof}{-1}\mbox{}\nolinebreak\hfill~%
  \ifnum \value{d@proof}=0{\qed}\else
    \ifnum \value{d@proof}=1{\hbox{\qed\nolinebreak\,\nolinebreak\qed}}\else
      \ifnum \value{d@proof}=2{\hbox{\qed\nolinebreak\,\nolinebreak\qed\nolinebreak\,\nolinebreak\qed}}\else
        {\hbox{\qed\nolinebreak...\nolinebreak\qed}}%
  \fi\fi\fi
  \medbreak
}
%*****************************
%!!
\renewcommand{\title}{}% {text \\of \\title}
\newcommand{\d@title}{}
\newcommand{\d@drtitle}{}
% VAR \d@title --command (global string to expand)
% VAR \d@drtitle --command (global string to expand)
%
\def\title#1{%
  \gdef\d@title{#1}\gdef\d@drtitle{#1}%
  \let\author\d@oldauthor
  \let\address\d@oldaddress
  \let\thanks\d@oldthanks
  \let\thanksmark\d@oldthanksmark
  \let\runningtitle\d@oldrunningtitle
  \let\runningauthors\d@oldrunningauthors
  \let\maketitle\d@oldmaketitle
  \def\title{\d@ahtwice}%
}
%!!clone of "\title"

%*****************************
%!!
\renewcommand{\author}{}% [list of p_labels]{name of 1 author}
\newcommand{\d@bauthor}{}\newcommand{\d@and}{}
\newcommand{\d@drauthor}{}\newcommand{\d@drand}{}
\newcommand{\d@btsc}{}% Platzhalter für \textsc
\newcommand{\orcidID}{}
% VAR \d@bauthor{} --command (string to expand)
% VAR \d@and{}     --command (string separating authors)
% VAR \d@drauthor  --command (string to expand)
% VAR \d@drand{}    --command (string separating running authors)
%
\def\author{\@ifnextchar[{\d@dauthor}{\d@sauthor}}
%!!clone of "\author"
\def\d@bauthor{}\def\d@and{}
\def\d@drauthor{}\def\d@drand{}

\def\d@btsc#1{\noexpand\d@btsc{#1}}
\def\d@orcidlogo#1{\noexpand\d@orcidlogo{#1}}
\def\d@orcidlink#1#2{\noexpand\d@orcidlink{#1}{#2}}
\newcommand{\bt@orcidfootnote}{}%
\newcommand{\bt@orcidfootnotesep}{}%
\newcommand{\bt@name}{}%
\newcommand{\bt@einzelorcidid}{}%
\newcount\bt@anzorcids
\newcount\bt@anzauthors
% VAR \bt@name          % name and orcid-logo for author-list
% VAR \bt@orcidfootnote % footnote with all author-orcidID-pairs
% VAR \bt@namemitorcid  % name with orcid-id and link, if given; name only, if not
% VAR \bt@nameohneorcid % name without orcid-id
% VAR \bt@einzelorcidid % last orcid-id

\newcommand{\bt@handlenameandorcid}[1]{%
  \advance\bt@anzauthors by 1
  \def\orcidID##1{\,\d@orcidlogo{##1}}%
  \edef\bt@name{#1}%
  \def\orcidID##1{:\! \d@orcidlink{https://orcid.org/##1}{##1}}%
  \edef\bt@namemitorcid{#1}%
  \def\orcidID##1{}%
  \edef\bt@nameohneorcid{#1}%
  \ifx\bt@namemitorcid\bt@nameohneorcid{}% no orcidID given
  \else% orcidID given
    \advance\bt@anzorcids by 1
    \xdef\bt@orcidfootnote{\bt@orcidfootnote\bt@orcidfootnotesep\bt@namemitorcid}%
    \xdef\bt@orcidfootnotesep{{}, }%
  \fi%
}

\newcommand{\d@dauthor}{}%--list of p_labels present
\def\d@dauthor[#1]#2{\d@thanksmark{#1}%
  \bt@handlenameandorcid{#2}%
  \xdef\d@bauthor{\d@bauthor\d@and\mbox{\d@btsc{\bt@name}}{}{\,\d@bthanksmark}}%
  \def\d@and{\hskip 1em\@plus.17fil{}}%
  \ifx\d@drauthor\empty%
    \gdef\d@drauthor{{\textsc{#2}}}%
  \else%
    \g@addto@macro\d@drauthor{\d@drand{\textsc{#2}}}% \g@add@macro extens a macro without expanding it
  \fi%
  \def\d@drand{{}, }%
}

\newcommand*{\d@sauthor}{}%--list of p_labels missing
\def\d@sauthor#1{%
  \bt@handlenameandorcid{#1}%
  \xdef\d@bauthor{\d@bauthor\d@and\mbox{\d@btsc{\bt@name}}{}{}}%
  \def\d@and{\hskip 1em\@plus.17fil{}}%
  \ifx\d@drauthor\empty%
    \gdef\d@drauthor{{\textsc{#1}}}%
  \else%
    \g@addto@macro\d@drauthor{\d@drand{\textsc{#1}}}% \g@add@macro extens a macro without expanding it
  \fi%
  \def\d@drand{{}, }%
}

\newcommand{\@OrigHeightRecip}{0.00390625} %1/256
\newlength{\@curXheight}\setlength{\@curXheight}{\fontcharht\font`X}

\newsavebox{\bt@orcidlogobox}
\savebox{\bt@orcidlogobox}{%
  %\includegraphics[bb=0 0 768 768, width=8pt]{ORCID-iD.png}
  \begin{tikzpicture}[yscale=-\@OrigHeightRecip*\@curXheight,xscale=\@OrigHeightRecip*\@curXheight,transform shape]%
    \pic{orcidlogo};%
  \end{tikzpicture}%
}
\def\bt@orcidlogoreal#1{%
  \raisebox{-.5pt}{\href{https://orcid.org/#1}{\usebox{\bt@orcidlogobox}}}%
  \gdef\bt@einzelorcidid{\href{https://orcid.org/#1}{#1}}%
}


%*****************************
%!!
\newcommand{\address}{}% [p_label]{text //of //address}
% VAR \d@baddress,\d@temp --boxes
%
\def\address{\@ifnextchar[{\d@daddress}{\d@saddress}}
\newsavebox{\d@baddress}\newsavebox{\d@temp}
\savebox{\d@baddress}[\linewidth][t]{\centering\normalsize}

\newcommand{\d@daddress}{}%--p_label present
\def\d@daddress[#1]#2{\d@label{#1}%
  \savebox{\d@temp}[\linewidth][t]{%
    \begin{minipage}[t]{\linewidth}\centering\small
      \usebox{\d@baddress}\\
      ${}^{(\d@ref{#1})}$\rule[0pt]{0pt}{3.5ex}{\textit{#2}}%
    \end{minipage}%
  }%
  \savebox{\d@baddress}[\linewidth][t]{\usebox{\d@temp}}%
}

\newcommand*{\d@saddress}[1]{%--p_label missing
  \savebox{\d@temp}[\linewidth][t]{%
    \begin{minipage}[t]{\linewidth}\centering\normalsize
      \usebox{\d@baddress}\\ \rule[0pt]{0pt}{3.5ex}{{\itshape #1}}%
    \end{minipage}%
  }%
  \savebox{\d@baddress}[\linewidth][t]{\usebox{\d@temp}}%
}

%*****************************
%!!Auxiliary support for \address
%
\newcommand*{\withinline}{\unskip\ -- \ignorespaces}

\newcommand{\email}{}% [short author's name]{email address text}
\def\email{\@ifnextchar[{\d@demail}{\d@semail}}

\newcommand{\d@demail}{}%--short author's name present
\def\d@demail[#1]#2{\mbox{%
  \hspace*{0.5em}{\small\emph{\texttt{#2} {(\textsc{#1})}}}\hspace*{0.5em}%
}}

\newcommand*{\d@semail}[1]{%--short author's name missing
\mbox{\hspace*{0.5em}{\small\emph{\texttt{#1}}}\hspace*{0.5em}}}

%*****************************
%!!
\renewcommand{\thanks}{}% [p_label]{text //to //footnote}
\def\thanks{\@ifnextchar[{\d@dthanks}{\d@sthanks}}
\renewcommand{\@thanks}{}\let\@thanks\relax %!!not used, cleared

\newcommand{\d@dthanks}{}%--p_label present
\long\def\d@dthanks[#1]#2{\d@label{#1}%
  \d@oldfootnotetext[0]{\hspace*{-1.8em}%
    \d@phantom{%!!
      \begin{minipage}[t]{\linewidth}\footnotesize
        \makebox[1.8em][r]{${}^{(\d@ref{#1})}$}\rule[1.7ex]{0em}{1ex}{#2}%
      \end{minipage}%
    }%!!end\d@phantom
  }%
}
%!!--space "1.8em" taken from "\def\@makefntext"

\newcommand{\d@sthanks}[1]{%--p_label missing
  \d@oldfootnotetext[0]{\hspace*{-1.8em}%
    \d@phantom{%!!
      \begin{minipage}[t]{\linewidth}\footnotesize
        \makebox[1.8em][r]{}\rule[1.7ex]{0em}{1ex}{#1}%
      \end{minipage}%
    }%!!end\d@phantom
  }%
}
%!!--space "1.8em" taken from "\def\@makefntext"

%*****************************
%!!
\newcommand{\thanksmark}{}% {list of p_labels}
\newcommand{\d@bthanksmark}{}\newcommand{\d@thanksmsep}{}
\newcommand{\d@thankslab}{}
% VAR \d@bthanksmark --command (global string to expand)
% VAR \d@thanksmsep  --command (string separating p_labels)
% VAR \d@thankslab   --command (loop control variable)
%
\def\thanksmark#1{\d@thanksmark{#1}\mbox{\d@bthanksmark}}

\newcommand*{\d@thanksmark}[1]{% {list of p_labels} => \d@bthanksmark
  \def\d@thanksmsep{}\def\d@bthanksmark{}%
  \@for\d@thankslab:=#1\do{%
    \xdef\d@bthanksmark{\d@bthanksmark\d@thanksmsep
      \d@ref{\d@thankslab}%
    }%
    \def\d@thanksmsep{,}%
  }%
  \xdef\d@bthanksmark{${}^{\scriptscriptstyle(\d@bthanksmark)}$}%
}

%*****************************
%!!
\newcommand{\runningtitle}{}% {text of running title}
\newcommand{\d@ertitle}{}\let\d@ertitle\relax
% VAR \d@ertitle --command (global string to expand)
%
\def\runningtitle#1{%
  \gdef\d@ertitle{#1}\def\runningtitle{\d@ahtwice}%
}

\newcommand{\runningauthors}{}% {text of running authors}
\newcommand{\d@erauthor}{}\let\d@erauthor\relax
% VAR \d@erauthor --command (global string to expand)
%
\def\runningauthors#1{%
  \gdef\d@erauthor{#1}\def\runningauthors{\d@ahtwice}%
}

%*****************************
%!!Auxiliary internal commands for preamble labels
%!!Counterparts of "\newlabel", "\label" and "\ref", via .aux file
%
\newcommand*{\dnewlabel}[1]{% {p_label}
\@ifundefined{c@#1}{%
  \stepcounter{footnote}\newcounter{#1}%
  \setcounter{#1}{\value{footnote}}%
}{}}
%!!--executed in .aux file, before preamble
%!!--counterpart of "\newlabel"

\newcommand*{\d@ref}[1]{% {p_label}
  \@ifundefined{c@#1}{{X}\write\@unused{JALC Class Warning:
    Preamble label `#1' undefined}}%
   {\ifnum \value{#1}=0{}\else {\Alph{#1}}\fi
  }%
}
%!!--detour by "\write", because of bug in "\@warning"
%!!--counterpart of "\ref"

\newcommand*{\d@label}[1]{% {p_label}
  \@ifundefined{c@#1}{\@warning{Preamble labels have changed^^J --
      re-run to get references right}%
    \newcounter{#1}\setcounter{#1}{24}%!!displayed as "X"
  }{}%
  \@bsphack
    \protected@write\@auxout{}{\string\dnewlabel{#1}}%
  \@esphack
}
%!!--clone of "\label"

%*****************************
%!!Auxiliary internal commands for warning messages
%
\newcommand*{\d@ahtitle}{%--warning: "ahead of \title"
  \@warning{Illegal command in preamble,}%
  \typeout{\space\space\space
    -- JALC document class prohibits some commands, until}%
  \typeout{\space\space\space\space\space\space\space\space
    \protect\title\space has been completed.}%
  \typeout{\space\space\space
    -- For proper formatting of the title page, see class
    documentation,}%
  \typeout{\space\space\space\space\space\space\space\space
    file `jalc-doc.pdf'.}%
}

\newcommand*{\d@ahmaketitle}{%--warning: "ahead of \maketitle"
  \@warning{Illegal command in preamble,}%
  \typeout{\space\space\space
    -- JALC document class prohibits some standard features}%
  \typeout{\space\space\space\space\space\space\space\space
    (like, e.g., abstract or standard \protect\footnote...
    handling), until}%
  \typeout{\space\space\space\space\space\space\space\space
    \protect\maketitle\space has been completed.}%
  \typeout{\space\space\space
    -- For proper formatting of the title page, see class
    documentation,}%
  \typeout{\space\space\space\space\space\space\space\space
    file `jalc-doc.pdf'.}%
}

\newcommand*{\d@ahtwice}{%--warning: "command used twice"
  \@warning{This command must not be used twice,^^J ignored}%
}

\newcommand*{\d@ahover}{%--warning: "below \maketitle"
  \@warning{JALC preamble command used below \protect\maketitle,}}

\newcommand*{\d@err}{%--error: "not allowed"
  \ClassError{jalc}{Some commands (\protect\and, \protect\marginpar,
    \protect\twocolumn\space ...)^^J are not allowed in jalc style,
    please fix the problem by yourself}%
  {see documentation of the jalc class, file `jalc-doc.pdf'}%
}

%*****************************
%!!
\renewcommand{\maketitle}{%!!modified clone
  \par\begingroup
    \def\@makefnmark{\hbox to\z@{$\m@th^{\@thefnmark}$\hss}}%
    \global\@topnum\z@%!!Prevents figures from going at top of page
    \@maketitle
  \endgroup
  \pagestyle{myheadings}\thispagestyle{empty}%
%!!Work done, cleaning up:
  \let\ds@sub\relax
  \let\d@phantom\relax
  \let\d@markboth\relax
  \def\title{\d@ahover}%
    \let\d@title\relax
    \let\d@drtitle\relax
  \def\author{\d@ahover}%
    \let\d@bauthor\relax
    \let\d@and\relax
    \let\d@drauthor\relax
    \let\d@drand\relax
    \let\d@dauthor\relax
    \let\d@sauthor\relax
    \let\d@oldauthor\relax
  \def\address{\d@ahover}%
    \savebox{\d@baddress}[0.0em][t]{}%
    \savebox{\d@temp}[0.0em][t]{}%
    \let\d@baddress\relax
    \let\d@temp\relax
    \let\d@daddress\relax
    \let\d@saddress\relax
    \let\d@oldaddress\relax
  %\def\withinline{\d@ahover} %!!Not off, on purpose!
  %\def\email{\d@ahover} %!!Not off, on purpose!
    %\let\d@demail\relax %!!Not off, on purpose!
    %\let\d@semail\relax %!!Not off, on purpose!
  \def\thanks{\d@ahover}%
    \let\d@dthanks\relax
    \let\d@sthanks\relax
    \let\d@oldthanks\relax
  \def\thanksmark{\d@ahover}%
    \let\d@bthanksmark\relax
    \let\d@thanksmsep\relax
    \let\d@thankslab\relax
    \let\d@thanksmark\relax
    \let\d@oldthanksmark\relax
  \def\runningtitle{\d@ahover}%
    \let\d@ertitle\relax
    \let\d@oldrunningtitle\relax
  \def\runningauthors{\d@ahover}%
    \let\d@erauthor\relax
    \let\d@oldrunningauthors\relax
  \let\d@ref\relax
  \let\d@label\relax
  \let\d@ahtitle\relax
  \gdef\d@ahmaketitle{}%
  \let\d@ahtwice\relax
  \let\@maketitle\relax
    \let\d@rbannr\relax
    \let\d@lbannr\relax
    \let\d@oldll\relax
    \let\d@oldnewline\relax
    \let\d@oldlinebreak\relax
  \let\d@oldmaketitle\relax
  %\let\dpagerange\relax %!!Not off, on purpose!
    %\let\c@dlastpage\relax %!!Not off, on purpose!
  \let\footnote\d@oldfootnote
  \let\footnotemark\d@oldfootnotemark
  \let\footnotetext\d@oldfootnotetext
  \let\d@oldfootnote\relax
  \let\d@oldfootnotemark\relax
  \let\d@oldfootnotetext\relax
  \def\thefootnote{\arabic{footnote}}%
  \setcounter{footnote}{0}%
  \renewcommand*{\pagestyle}[1]{}% %!!\thispagestyle allowed
  \renewcommand{\markright}[1]{}%
  \renewcommand{\markboth}[2]{}%
  \typeout{\space\space\space\space...done}%
  \def\maketitle{\d@ahover}%
}
%!!clone of "\maketitle"

\newcommand{\bt@checkbannrok}{}

\renewcommand{\@maketitle}{%!!modified clone
  \typeout{JALC: Building title page...}%
  %\newpage\null\mbox{}\vspace{-2.30cm}\par%
  \d@bannr\vspace{10mm}\par
  \begin{center}%
    \def\thanksmark##1{\@@warning{thanksmark in illegal
        location !!!}[!!!!
        $\backslash$thanksmark in illegal location !!!!]}%
      %!!set up running title and running author(s):
      %!!turn off "\\", "\newline", "\linebreak":
        \let\d@oldll\\ \def\\{\unskip\ \ignorespaces}%
        \let\d@oldnewline\newline
          \def\newline{\unskip\ \ignorespaces}%
        \let\d@oldlinebreak\linebreak
          \def\linebreak{\unskip\ \ignorespaces}%
        \typeout{JALC: Preparing title and author(s) for running
          headlines...}%
        \@ifundefined{d@ertitle}{}{\gdef\d@drtitle{\d@ertitle}}%
        \@ifundefined{d@erauthor}{}{\gdef\d@drauthor{\d@erauthor}}%
        \d@markboth{\d@drauthor}{\d@drtitle}%
        %!!testing correctness of running author(s) and running title:
        \sbox{\d@temp}{\d@drauthor}\sbox{\d@temp}{\d@drtitle}%
      %!!turn on "\\", "\newline", "\linebreak":
      \let\\\d@oldll
        \let\newline\d@oldnewline \let\linebreak\d@oldlinebreak
      \typeout{JALC: Preparing title for the first page...}%
      \def\\{\protect\d@oldll}% make linebreak robust
      {\large\bfseries \MakeTextUppercase{\d@title}}\vspace{10mm}\par
      \typeout{JALC: Preparing author(s) for the first page...}%
      \d@phantom{%!!
        \let\d@btsc\textsc%
        \let\d@orcidlogo\bt@orcidlogoreal%
        \begin{minipage}[t]{0.9\linewidth}\centering\small
          \d@bauthor{}\mbox{}\\[-1.3ex]%
          \mbox{}%
        \end{minipage}%
      }%!!end\d@phantom
      \let\d@orcidlink\href%
      \ifx\bt@orcidfootnote\empty{}%
      \else%
        \ifnum\bt@anzauthors>1%
          \ifnum\bt@anzorcids>0%
            \d@oldfootnotetext[0]{\hspace*{-1.3em}\raisebox{-.5pt}{\usebox{\bt@orcidlogobox}}\:\bt@orcidfootnote}%
          \fi%
        \else%
          \ifnum\bt@anzorcids>0%
            \d@oldfootnotetext[0]{\hspace*{-1.3em}\raisebox{-.5pt}{\usebox{\bt@orcidlogobox}}\:\bt@einzelorcidid}%
          \fi%
        \fi%
      \fi%
    \let\thanksmark\d@oldthanksmark
    \par
    \typeout{JALC: Preparing addresses...}%
    \d@phantom{%!!
      \usebox{\d@baddress}%
    }%!!end\d@phantom
  \end{center}%
  \mbox{}\par
}
%!!clone of "\@maketitle"

\newcommand\biblio[1]{\bibliographystyle{jalc}\pdfbookmark{\refname}{\refname}
{\small\bibliography{#1}}}

%*****************************
%!!Small extensions to the standard article
%!!(except for preamble and theorem-like environments)
%
\renewenvironment{abstract}{%
  \@ifundefined{@maketitle}{}{\d@ahmaketitle}%
  \begin{quotation}\footnotesize\baselineskip9pt%
    \noindent\mbox{}\hfill ABSTRACT\hfill\mbox{}\\[0.8mm]}%
{\unskip\end{quotation}\ignorespaces}

\newcommand*{\keywords}{\unskip\mbox{}\\ \mbox{}\\
  \textit{Keywords:}\hspace{\labelsep}\ignorespaces}

%*****************************
%!!Global initial declarations
%
%!!just for using the fact that \roman{0}=blank :
\renewcommand*{\thefootnote}{\roman{footnote}}
\setcounter{footnote}{0}

\newcommand*{\d@oldll}{}
\newcommand*{\d@oldnewline}{}
\newcommand*{\d@oldlinebreak}{}
\newcommand*{\d@oldauthor}{}
\newcommand*{\d@oldaddress}{}
\newcommand*{\d@oldthanks}{}
\newcommand*{\d@oldthanksmark}{}
\newcommand*{\d@oldrunningtitle}{}
\newcommand*{\d@oldrunningauthors}{}
\newcommand*{\d@oldmaketitle}{}
\newcommand*{\d@oldfootnote}{}
\newcommand*{\d@oldfootnotemark}{}
\newcommand*{\d@oldfootnotetext}{}

\let\d@oldauthor\author
\let\d@oldaddress\address
\let\d@oldthanks\thanks
\let\d@oldthanksmark\thanksmark
\let\d@oldrunningtitle\runningtitle
\let\d@oldrunningauthors\runningauthors
\let\d@oldmaketitle\maketitle
\let\d@oldfootnote\footnote
\let\d@oldfootnotemark\footnotemark
\let\d@oldfootnotetext\footnotetext

\def\author{\d@ahtitle}
\def\address{\d@ahtitle}
\def\thanks{\d@ahtitle}
\def\thanksmark{\d@ahtitle}
\def\runningtitle{\d@ahtitle}
\def\runningauthors{\d@ahtitle}
\def\maketitle{\d@ahtitle}
\def\footnote{\d@ahmaketitle}
\def\footnotemark{\d@ahmaketitle}
\def\footnotetext{\d@ahmaketitle}

\relpenalty=10000
\binoppenalty=10000

%%**********************************
\endinput
