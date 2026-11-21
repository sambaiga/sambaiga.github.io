---
name: site-writing
description: Writing standard for the copy of sambaiga.github.io (pages, descriptions, blog titles, book and software cards). Use before writing or editing any visitor-facing text on the site, and again before showing the result.
---

# Site writing standard

The site reads in the register of the author's thesis and books: formal, concise, specific and in the first person
singular where the author speaks. It is borrowed from the umeme book (`scripts/stylecheck.py` there) and enforced here
by `scripts/stylecheck.py`, run by the `site-copy-style` pre-commit hook.

## Rules

1. **Formal register.** No contractions, no conversational phrases ("let's", "of course", "actually", "really", "a lot of").
2. **No second person.** Describe what the post, page or tool does, not what "you" will get. Write "This post describes",
   not "Learn how" or "gives you".
3. **No dashes as punctuation.** Use a comma, a colon or a new sentence. No em- or en-dash.
4. **No marketing words.** No "seamless", "cutting-edge", "unlock", "empower", "journey", "genuinely", "majestic",
   "game-changing". State the capability instead.
5. **Checkable facts only.** A figure on the site must be countable from the repositories, the publication list or Google
   Scholar. No "100% satisfied" or "projects delivered".
6. **Descriptive headings and titles.** Noun phrases, not questions or imperatives; no "Why Your X Is Failing".
7. **Specific descriptions.** One or two sentences: the subject, the method or tool, the result or use. A software card says
   what the library does and for which models or data, taken from its README.
8. **Concept first, claim second.** Say what a thing is before what it is good for; no result before its definition.
9. **Vary the sentences.** Avoid runs of short staccato sentences, announcing sentences ("In this section we will") and
   rhetorical questions. Read the paragraph aloud as the author would.
10. **Names.** The page is "Blog" (not "Writing"); the libraries are Twiga, Milia, Popo, Kobe, Kinyonga.

## Checks

- `python scripts/stylecheck.py [files]` lists `file:line: reason`; the pre-commit hook runs it on changed copy files.
- Talk and paper titles are quoted from the originals and are not checked. Blog post bodies are not checked, only their
  title, description and subtitle.
- Before showing copy, reread it for the tells a checker cannot catch: triplets of adjectives, "not only ... but also",
  a closing sentence that restates the paragraph, and vague nouns ("solutions", "approaches") without a specific.

## Origin

Rules 1 to 3, the banned list and the heading rule come from the umeme book; rules 4, 5 and 10 are site-specific.
