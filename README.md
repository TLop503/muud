# M.U.U.D. (MarkUpUpDownDown)

M.U.U.D. is (going to be) a python package for converting all the markup languages to all the other markup languages.

Currently Suported:
- Nothing

Planned Support:
- [M.U.U.D.I.](#muudi-markupupdowndown-internal)
- ReStructuredText
- Markdown
- HTML
- JSON ? (probably not)
- YAML?

### These are exteremly subject to change. 

# M.U.U.D.I. (MarkUpUpDownDown Internal)

M.U.U.D.I. is the internal staging markup language for M.U.U.D. It isn't intended to actually be used to render docs, but instead to be used as a staging language for converting between other markup languages. Conversion happens by converting to M.U.U.D.I. and then to the target language, to avoid having to write a converter for every language to every other language. M.U.U.D.I. Is dictionsary based, and is intended to be easy to convert to and from.

While I hope to make M.U.U.D.I. as lossless as possible, it is not intended to be a perfect conversion. It is intended to be a good enough conversion, and to be easy to convert to and from.
