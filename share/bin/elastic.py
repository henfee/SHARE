import json

from share.bin.util import command

from bots.elasticsearch import tasks
from bots.elasticsearch.bot import ElasticSearchBot


@command('Manage Elasticsearch')
def search(args, argv):
    """
    Usage:
        {0} search <command> [<args>...]
        {0} search [--help | --filter=FILTER | --all] [options]

    Options:
        -h, --help           Show this screen.
        -f, --filter=FILTER  Filter the queryset to be index using this filter. Must be valid JSON.
        -a, --all            Index everything. Equivalent to --filter '{{"id__isnull": false}}'.
        -u, --url=URL        The URL of Elasticsearch.
        -i, --index=INDEX    The name of the Elasticsearch index to use.
        -a, --async          Send an update_elasticsearch task to Celery.

    Commands:
    {1.subcommand_list}

    See '{0} search <command> --help' for more information on a specific command.
    """

    if args['--filter']:
        args['--filter'] = json.loads(args['--filter'])

    if args['--all']:
        args['--filter'] = {'id__isnull': False}

    kwargs = {
        'filter': args.get('--filter'),
        'index': args.get('--index'),
        'url': args.get('--url'),
        # 'models': args.get('--models'),
    }

    if args['--async']:
        tasks.update_elasticsearch.apply_async((), kwargs)
    else:
        tasks.update_elasticsearch(**kwargs)


@search.subcommand('Drop the Elasticsearch index')
def purge(args, argv):
    """
    Usage: {0} search purge

    NOT YET IMPLEMENTED
    """
    raise NotImplementedError()


@search.subcommand('Synchronize the Elasticsearch index and database')
def janitor(args, argv):
    """
    Usage: {0} search janitor [--dry | --async] [options]

    Options:
        -u, --url=URL        The URL of Elasticsearch.
        -i, --index=INDEX    The name of the Elasticsearch index to use.
    """
    kwargs = {
        'es_url': args['--url'],
        'es_index': args['--index'],
        'dry': bool(args['--dry']),
    }

    if args['--async']:
        tasks.elasticsearch_janitor.apply_async((), kwargs)
    else:
        tasks.elasticsearch_janitor(**kwargs)


@search.subcommand('Create indicies and apply mappings')
def setup(args, argv):
    """
    Usage: {0} search setup
    """
    ElasticSearchBot().setup()
