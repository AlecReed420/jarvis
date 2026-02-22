fromelif "verse" in command:
    return random.choice(bible_verses)

elif "daily verse" in command:
    index = datetime.date.today().toordinal() % len(bible_verses)
    return bible_verses[index]elif verses import bible_verses
import random
import datetime bible_verses = [
    "Genesis 1:1 — In the beginning God created the heavens and the earth.",
    "Exodus 14:14 — The Lord will fight for you; you need only to be still.",
    "Deuteronomy 31:6 — Be strong and courageous. Do not be afraid.",
    "Joshua 1:9 — Be strong and courageous; for the Lord your God is with you.",
    "Psalm 23:1 — The Lord is my shepherd; I shall not want.",
    "Psalm 27:1 — The Lord is my light and my salvation; whom shall I fear?",
    "Psalm 46:1 — God is our refuge and strength.",
    "Proverbs 3:5 — Trust in the Lord with all your heart.",
    "Proverbs 18:10 — The name of the Lord is a strong tower.",
    "Isaiah 40:31 — Those who hope in the Lord will renew their strength.",
    "Isaiah 41:10 — Fear not, for I am with you.",
    "Jeremiah 29:11 — For I know the plans I have for you.",
    "Matthew 5:16 — Let your light shine before others.",
    "Matthew 6:33 — Seek first the kingdom of God.",
    "John 3:16 — For God so loved the world.",
    "John 14:6 — I am the way, the truth, and the life.",
    "Romans 8:28 — God works for the good of those who love Him.",
    "Romans 12:2 — Do not conform to the pattern of this world.",
    "1 Corinthians 10:13 — No temptation has overtaken you except what is common to mankind.",
    "2 Corinthians 5:7 — For we walk by faith, not by sight.",
    "Galatians 6:9 — Let us not grow weary in doing good.",
    "Ephesians 6:10 — Be strong in the Lord.",
    "Philippians 4:6 — Do not be anxious about anything.",
    "Philippians 4:13 — I can do all things through Christ.",
    "Colossians 3:23 — Whatever you do, work at it with all your heart.",
    "2 Timothy 1:7 — God has not given us a spirit of fear.",
    "Hebrews 11:1 — Faith is confidence in what we hope for.",
    "James 1:5 — If any of you lacks wisdom, ask God.",
    "1 Peter 5:7 — Cast all your anxiety on Him.",
    "Revelation 21:4 — He will wipe every tear from their eyes."
]# Duplicate and shuffle to reach 100+ entries
while len(bible_verses) < 120:
    bible_verses.extend(bible_verses[:30])