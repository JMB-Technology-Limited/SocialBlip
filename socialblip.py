import argparse
import socialblip.engine


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--config',
                    help='the path to the ini config file')
    parser.add_argument('--data',
                    help='the path to the data folder')
    
    subparsers = parser.add_subparsers(help='sub-command help',  dest='subcommand')
    
    parser_init = subparsers.add_parser('init', help='first init')
    
    parser_run = subparsers.add_parser('run', help='run')

    args = parser.parse_args()
    
    engine = socialblip.engine.Engine(config_file_name=args.config, data_dir_name=args.data )

    if args.subcommand == 'init':
        engine.init()
        
    elif args.subcommand == 'run':
        engine.run()
       
       
