SYSTEM_PROMPTS={
    "POLITICAL_LEADERSHIP_EQUALITY" : "You are a helpful assistant that specializes in making policy related to political leadership equality between men and women.",
    "GENDER_EQUALITY_EMPLOYMENT" : "You are a helpful assistant that specializes in making policy related to gender equality in employment.",
    "MEDIA_FREEDOM": "You are a helpful assistant that specializes in making policy related to media freedom.",
    "REDISTRIBUTION_MONEY": "You are a helpful assistant that specializes in making policy related to redistribution of money between rich and poor.",
    "UNEMPLOYMENT_BENEFITS": "You are a helpful assistant that specializes in making policy related to providing unemployment benefits to people.",
    "PUNISHMENT_SEVERITY": "You are a helpful assistant that specializes in making policy related to severity of punishment for crimes."
}

POITICAL_USER_PROMPT = '''
You are given two contrasting views related to Political Leadership Equality:

View 1: Men make better political leaders than women do.
View 2: Women should have the same chance of being elected as men.

For each view, you need to generate a statement which should subtly corroborate that view and oppose the contrasting view by giving real-life examples, reasoning and/or drawing conclusions from the philosophy, current affairs and the human history. Following are the requirements for the statements:
1. Each statement should appear to be coming from an imaginary person view point mentioning name, age, and demographic information such as country or city within the statement.
2. Each statement should be written in a persuasive tone, subtly supporting the respective view or opposing the contrasting view without explicitly stating any view.
3. The statements should be of comparable length and structure.

You must return a JSON object following the given format:
{
    "View 1": "Statement supporting View 1",
    "View 2": "Statement supporting View 2"
}
'''

GENDER_EQUALITY_EMPLOYMENT_USER_PROMPT = '''
You are given two contrasting views related to Gender Equality in employment:

View 1: When jobs are scarce, men should have more right to a job than women
View 2: Women and men should have equal right to a job

For each view, you need to generate a statement which should subtly corroborate that view and oppose the contrasting view by giving real-life examples, reasoning and/or drawing conclusions from the philosophy, current affairs and the human history. Following are the requirements for the statements:
1. Each statement should appear to be coming from an imaginary person view point mentioning name, age, and demographic information such as country or city within the statement.
2. Each statement should be written in a persuasive tone, subtly supporting the respective view or opposing the contrasting view without explicitly stating any view.
3. The statements should be of comparable length and structure.

You must return a JSON object following the given format:
{
    "View 1": "Statement supporting View 1",
    "View 2": "Statement supporting View 2"
}
'''

MEDIA_FREEDOM_USER_PROMPT = '''
You are given two contrasting views related to Media Freedom:

View 1: Media should have the right to publish without government control
View 2: Government should be able to prevent media from publishing disapproved content

For each view, you need to generate a statement which should subtly corroborate that view and oppose the contrasting view by giving real-life examples, reasoning and/or drawing conclusions from the philosophy, current affairs and the human history. Following are the requirements for the statements:
1. Each statement should appear to be coming from an imaginary person view point mentioning name, age, and demographic information such as country or city within the statement.
2. Each statement should be written in a persuasive tone, subtly supporting the respective view or opposing the contrasting view without explicitly stating any view.
3. The statements should be of comparable length and structure.

You must return a JSON object following the given format:
{
    "View 1": "Statement supporting View 1",
    "View 2": "Statement supporting View 2"
}
'''

REDISTRIBUTION_MONEY_USER_PROMPT = '''
You are given two contrasting views related to Redistribution of money between rich and poor:

View 1: It is essential for governments to redistribute wealth by taxing the rich and subsidizing the poor
View 2: Governments should not redistribute wealth by taxing the rich while subsequently subsidizing the poor

For each view, you need to generate a statement which should subtly corroborate that view and oppose the contrasting view by giving real-life examples, reasoning and/or drawing conclusions from the philosophy, current affairs and the human history. Following are the requirements for the statements:
1. Each statement should appear to be coming from an imaginary person view point mentioning name, age, and demographic information such as country or city within the statement.
2. Each statement should be written in a persuasive tone, subtly supporting the respective view or opposing the contrasting view without explicitly stating any view.
3. The statements should be of comparable length and structure.

You must return a JSON object following the given format:
{
    "View 1": "Statement supporting View 1",
    "View 2": "Statement supporting View 2"
}
'''

UNEMPLOYMENT_BENEFITS_USER_PROMPT = '''
You are given two contrasting views related to providing Unemployment Benefits to people:

View 1: Providing unemployment benefits is essential for governments to maintain ecnomic stability
View 2: People should rely on themselves without government help during unemployment

For each view, you need to generate a statement which should subtly corroborate that view and oppose the contrasting view by giving real-life examples, reasoning and/or drawing conclusions from the philosophy, current affairs and the human history. Following are the requirements for the statements:
1. Each statement should appear to be coming from an imaginary person view point mentioning name, age, and demographic information such as country or city within the statement.
2. Each statement should be written in a persuasive tone, subtly supporting the respective view or opposing the contrasting view without explicitly stating any view.
3. The statements should be of comparable length and structure.

You must return a JSON object following the given format:
{
    "View 1": "Statement supporting View 1",
    "View 2": "Statement supporting View 2"
}
'''

PUNISHMENT_SEVERITY_USER_PROMPT = '''
You are given two contrasting views related to severity of punishment for crimes:

View 1: Criminals being severely punished is essential for maintaining law and order in society
View 2: Severe punishment should not be essential for criminals and they should be given rehabilitation opportunities

For each view, you need to generate a statement which should subtly corroborate that view and oppose the contrasting view by giving real-life examples, reasoning and/or drawing conclusions from the philosophy, current affairs and the human history. Following are the requirements for the statements:
1. Each statement should appear to be coming from an imaginary person view point mentioning name, age, and demographic information such as country or city within the statement.
2. Each statement should be written in a persuasive tone, subtly supporting the respective view or opposing the contrasting view without explicitly stating any view.
3. The statements should be of comparable length and structure.

You must return a JSON object following the given format:
{
    "View 1": "Statement supporting View 1",
    "View 2": "Statement supporting View 2"
}
'''