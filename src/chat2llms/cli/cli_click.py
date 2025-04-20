import click

from ..model_response import OpenAIResponse, GeminiResponse
from ..analyzer import AnswerAnalyzer
from ..base_client import BaseClient

SUPPORTED_MODELS = {
    "gemini": lambda: BaseClient("gemini"),
    "deepseek": lambda: BaseClient("deepseek"),
    "openai": lambda: BaseClient("openai"),
    "grok": lambda: BaseClient("grok")
}

@click.command()
@click.option('--model1', required=True, help='Name of the first model（ie. openai）')
@click.option('--model2', required=True, help='Name of the second model（ie gemini）')
@click.option('--prompt', required=True, help='the prompt string')
def main(model1, model2, prompt):
    if model1 not in SUPPORTED_MODELS or model2 not in SUPPORTED_MODELS:
        click.echo(f"❌ Now the model is not suported, select from: {', '.join(SUPPORTED_MODELS.keys())}")
        return

    client1 = SUPPORTED_MODELS[model1]()
    client2 = SUPPORTED_MODELS[model2]()

    if model1 == "gemini":
        r1 = GeminiResponse(client1)
    else:
        r1 = OpenAIResponse(client1)

    if model2 == "gemini":
        r2 = GeminiResponse(client2)
    else:
        r2 = OpenAIResponse(client2)

    click.secho(f"\n=== Prompt ===", fg='cyan', bold=True)
    click.echo(prompt)

    click.secho(f"\n=== {model1.upper()} Response ===", fg='cyan', bold=True)
    click.echo(r1.get_response(prompt))

    click.secho(f"\n=== {model2.upper()} Response ===", fg='magenta', bold=True)
    click.echo(r2.get_response(prompt))

    analyzer = AnswerAnalyzer(r1, r2)

    click.secho(f"\n=== Text Similarity ===", fg='yellow', bold=True)    
    click.echo(analyzer.compute_similarity())    

    click.secho(f"\n=== Semantic Similarity ===", fg='yellow', bold=True)    
    click.echo(analyzer.compute_semantic_similarity())    

    click.secho(f"\n=== Highlight of Differences ===", fg='yellow', bold=True)    
    click.echo(analyzer.highlight_differences())    

if __name__ == '__main__':
    main()
