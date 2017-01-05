def get_config_zh2en():
    config = {}

    # Model related -----------------------------------------------------------

    # Sequences longer than this will be discarded
    config['seq_len'] = 50

    # Number of hidden units in encoder/decoder GRU
    config['enc_nhids'] = 1000
    config['dec_nhids'] = 1000

    # Dimension of the word embedding matrix in encoder/decoder
    config['enc_embed'] = 620
    config['dec_embed'] = 620

    # Where to save model, this corresponds to 'prefix' in groundhog
    config['saveto'] = 'search_model_zh2en'

    # Optimization related ----------------------------------------------------

    # Batch size
    config['batch_size'] = 80

    # This many batches will be read ahead and sorted
    config['sort_k_batches'] = 12

    # Optimization step rule
    config['step_rule'] = 'AdaDelta'

    # Gradient clipping threshold
    config['step_clipping'] = 1.

    # Std of weight initialization
    config['weight_scale'] = 0.01

    # Regularization related --------------------------------------------------

    # Weight noise flag for feed forward layers
    config['weight_noise_ff'] = False

    # Weight noise flag for recurrent layers
    config['weight_noise_rec'] = False

    # Dropout ratio, applied only after readout maxout
    config['dropout'] = 1.0

    # Vocabulary/dataset related ----------------------------------------------

    # Root directory for dataset
    datadir = 'machine_translation/data/'

    # Module name of the stream that will be used
    config['stream'] = 'stream'

    # Source and target vocabularies
    config['src_vocab'] = datadir + 'vocab.zh-en.zh.pkl'
    config['trg_vocab'] = datadir + 'vocab.zh-en.en.pkl'

    # Source and target datasets
    config['src_data'] = datadir + 'train.zh-en.zh.tok.shuf'
    config['trg_data'] = datadir + 'train.zh-en.en.tok.shuf'

    # Source and target vocabulary sizes, should include bos, eos, unk tokens
    config['src_vocab_size'] = 30000
    config['trg_vocab_size'] = 30000

    # Special tokens and indexes
    config['unk_id'] = 1
    config['bos_token'] = '<S>'
    config['eos_token'] = '</S>'
    config['unk_token'] = '<UNK>'

    # Early stopping based on bleu related ------------------------------------

    # Normalize cost according to sequence length after beam-search
    config['normalized_bleu'] = True

    # Bleu script that will be used (moses multi-perl in this case)
    config['bleu_script'] = datadir + 'multi-bleu.perl'

    # Validation set source file
    config['val_set'] = datadir + 'devset/devset1_2.zh'

    # Validation set gold file
    config['val_set_grndtruth0'] = datadir + 'devset/devset1_2.lc.en0'
    config['val_set_grndtruth1'] = datadir + 'devset/devset1_2.lc.en1'
    config['val_set_grndtruth2'] = datadir + 'devset/devset1_2.lc.en2'
    config['val_set_grndtruth3'] = datadir + 'devset/devset1_2.lc.en3'
    config['val_set_grndtruth4'] = datadir + 'devset/devset1_2.lc.en4'
    config['val_set_grndtruth5'] = datadir + 'devset/devset1_2.lc.en5'
    config['val_set_grndtruth6'] = datadir + 'devset/devset1_2.lc.en6'
    config['val_set_grndtruth7'] = datadir + 'devset/devset1_2.lc.en7'
    config['val_set_grndtruth8'] = datadir + 'devset/devset1_2.lc.en8'
    config['val_set_grndtruth9'] = datadir + 'devset/devset1_2.lc.en9'
    config['val_set_grndtruth10'] = datadir + 'devset/devse1_2.lc.en10'
    config['val_set_grndtruth11'] = datadir + 'devset/devse1_2.lc.en11'
    config['val_set_grndtruth12'] = datadir + 'devset/devset1_2.lc.en12'
    config['val_set_grndtruth13'] = datadir + 'devset/devset1_2.lc.en13'
    config['val_set_grndtruth14'] = datadir + 'devset/devset1_2.lc.en14'
    config['val_set_grndtruth15'] = datadir + 'devset/devset1_2.lc.en15'

    # Test set source file
    config['test_set'] = datadir + 'devset/devset3.zh'

    # Test set gold file
    config['test_set_grndtruth0'] = datadir + 'devset/devset3.lc.en0'
    config['test_set_grndtruth1'] = datadir + 'devset/devset3.lc.en1'
    config['test_set_grndtruth2'] = datadir + 'devset/devset3.lc.en2'
    config['test_set_grndtruth3'] = datadir + 'devset/devset3.lc.en3'
    config['test_set_grndtruth4'] = datadir + 'devset/devset3.lc.en4'
    config['test_set_grndtruth5'] = datadir + 'devset/devset3.lc.en5'
    config['test_set_grndtruth6'] = datadir + 'devset/devset3.lc.en6'
    config['test_set_grndtruth7'] = datadir + 'devset/devset3.lc.en7'
    config['test_set_grndtruth8'] = datadir + 'devset/devset3.lc.en8'
    config['test_set_grndtruth9'] = datadir + 'devset/devset3.lc.en9'
    config['test_set_grndtruth10'] = datadir + 'devset/devse3.lc.en10'
    config['test_set_grndtruth11'] = datadir + 'devset/devse3.lc.en11'
    config['test_set_grndtruth12'] = datadir + 'devset/devset3.lc.en12'
    config['test_set_grndtruth13'] = datadir + 'devset/devset3.lc.en13'
    config['test_set_grndtruth14'] = datadir + 'devset/devset3.lc.en14'
    config['test_set_grndtruth15'] = datadir + 'devset/devset3.lc.en15'

    # Print validation output to file
    config['output_val_set'] = True

    # Validation output file
    config['val_set_out'] = config['saveto'] + '/validation_out.txt'

    # Test output file
    config['test_set_out'] = config['saveto'] + '/test_out.txt'

    # Beam-size
    config['beam_size'] = 12

    # Timing/monitoring related -----------------------------------------------

    # Maximum number of updates
    config['finish_after'] = 100000

    # Reload model from files if exist
    config['reload'] = True

    # Save model after this many updates
    config['save_freq'] = 500

    # Show samples from model after this many updates
    config['sampling_freq'] = 13

    # Show this many samples at each sampling
    config['hook_samples'] = 2

    # Validate bleu after this many updates
    config['bleu_val_freq'] = 5000

    # Start bleu validation after this many updates
    config['val_burn_in'] = 10000

    return config
