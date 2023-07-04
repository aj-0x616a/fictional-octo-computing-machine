import click
import nltk
#nltk.download('punkt')
#nltk.download("stopwords")


@click.group(invoke_without_command=True)
@click.option("--debug/--no-debug")
@click.pass_context
def main(ctx: click.Context, debug: bool) -> None:
    """
    main command
    """
    ctx.obj = {"debug": debug}

    if ctx.invoked_subcommand is None:
        click.echo("Hello World!")


@main.command()
@click.pass_obj
def tokenizing(ctx: dict) -> None:
    """
    Example of tokenizing using nltk
    """

    example_string = """
    Muad'Dib learned rapidly because his first training was in how to learn.
    And the first lesson of all was the basic trust that he could learn.
    It's shocking to find how many people do not believe they can learn,
    and how many more believe learning to be difficult. 
    """
    
    click.echo("** tokenize by word **")
    click.echo(nltk.word_tokenize(example_string))
    
    click.echo("** tokenize by sentence **")
    click.echo(nltk.sent_tokenize(example_string))


@main.command()
@click.pass_obj
def filteringstopwords(ctx: dict) -> None:
    from nltk.corpus import stopwords
    """
    Example of filtering stopwords using nltk
    """

    worf_quote = "Sir, I protest. I am not a merry man!"
    words_in_quote = nltk.word_tokenize(worf_quote)

    click.echo(words_in_quote)
    stop_words = set(stopwords.words("english"))

    # List comprehension
    """
    The provided code utilizes a list comprehension to filter out specific words from the words_in_quote list based on certain conditions. Let's break down the code snippet step by step:

    filtered_list = [... for word in words_in_quote if word.casefold() not in stop_words]:
    This line creates a new list called filtered_list using a list comprehension. It iterates over each word in the words_in_quote list and applies a condition to filter out unwanted words. Here's how the comprehension works:
        The expression word for word in words_in_quote specifies the elements to include in the new list. It simply takes each word from the words_in_quote list.
        The if word.casefold() not in stop_words condition filters out words that are present in the stop_words list. The word.casefold() method converts the word to lowercase for case-insensitive comparison. If the lowercase version of the word is not found in the stop_words list, the word is included in the filtered_list.

    click.echo(filtered_list):
    This line uses click.echo() to print the filtered_list to the console. It outputs the filtered list of words.

In summary, the code filters out specific words from the words_in_quote list using a list comprehension. The filtered words are stored in the filtered_list variable. Finally, the filtered_list is printed to the console using click.echo().
    """
    filtered_list = [
        word for word in words_in_quote if word.casefold() not in stop_words
    ]
    click.echo(filtered_list)

@main.command()
@click.pass_obj
def stemming(ctx: dict) -> None:
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize
    stemmer = PorterStemmer()
    string_for_stemming = """
    The crew of the USS Discovery discovered many discoveries.
    Discovering is what explorers do.
    """
    words = word_tokenize(string_for_stemming)
    stemmed_words = [stemmer.stem(word) for word in words]
    click.echo(stemmed_words)


if __name__ == "__main__":
    main(obj={})
