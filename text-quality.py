from textstat import textstat

text = "The quick brown fox jumps over the lazy dog."
hard_text = "Though amid all the smoking horror and diabolism of a sea-fight, sharks will be seen longingly gazing up to the ship’s decks, like hungry dogs round a table where red meat is being carved, ready to bolt down every killed man that is tossed to them; and though, while the valiant butchers over the deck-table are thus cannibally carving each other’s live meat with carving-knives all gilded and tasselled, the sharks, also, with their jewel-hilted mouths, are quarrelsomely carving away under the table at the dead meat."

""" 
From https://en.wikipedia.org/wiki/Flesch–Kincaid_readability_tests 
Score	School level (US)	Notes
100.00–90.00	5th grade	Very easy to read. Easily understood by an average 11-year-old student.
90.0–80.0	6th grade	Easy to read. Conversational English for consumers.
80.0–70.0	7th grade	Fairly easy to read.
70.0–60.0	8th & 9th grade	Plain English. Easily understood by 13- to 15-year-old students.
60.0–50.0	10th to 12th grade	Fairly difficult to read.
50.0–30.0	College	Difficult to read.
30.0–10.0	College graduate	Very difficult to read. Best understood by university graduates.
10.0–0.0	Professional	Extremely difficult to read. Best understood by university graduates. """

print("Test\tv1\tv2\tv3\taverage")
print("flesch_reading_ease\t")
print("easy:",textstat.flesch_reading_ease(text))
print("hard:",textstat.flesch_reading_ease(hard_text))

print("\nflesch_kincaid_grade")
print("easy:",textstat.flesch_kincaid_grade(text))
print("hard:",textstat.flesch_kincaid_grade(hard_text))

print("\ngunning_fog")
print("easy:",textstat.gunning_fog(text))
print("hard:",textstat.gunning_fog(hard_text))

print("\ncoleman_liau_index")
print("easy:",textstat.coleman_liau_index(text))
print("hard:",textstat.coleman_liau_index(hard_text))

print("\nlinsear_write_formula")
print("easy:",textstat.linsear_write_formula(text))
print("hard:",textstat.linsear_write_formula(hard_text))

print("\ndale_chall_readability_score")
print("easy:",textstat.dale_chall_readability_score(text))
print("hard:",textstat.dale_chall_readability_score(hard_text))

print("\ndifficult_words")
print("easy:",textstat.difficult_words(text), textstat.difficult_words_list(text))
print("hard:",textstat.difficult_words(hard_text), textstat.difficult_words_list(hard_text))

