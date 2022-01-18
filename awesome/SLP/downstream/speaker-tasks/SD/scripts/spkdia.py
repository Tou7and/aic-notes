import torchaudio
from speechbrain.lobes.features import Fbank
from speechbrain.processing.features import InputNormalization
from speechbrain.lobes.models.Xvector import Xvector

def compute_embeddings(wavs, wav_lens=None, device="cpu"):
    """Definition of the steps for computation of embeddings from the waveforms
    """
    # Assign full length if wav_lens is not assigned
    if wav_lens is None:
        wav_lens = torch.ones(wavs.shape[0], device=self.device)

    with torch.no_grad():
        feats_extractor = Fbank(n_mels=24)
        normalizer = InputNormalization(norm_type='sentence', std_norm=False)
        xvector_extractor = Xvector()
        emb_normalizer = InputNormalization(norm_type='global', std_norm=False)

        wavs = wavs.to(device)
        feats = Fbank(wavs)
        lens = torch.ones(feats.shape[0], device=device)
        feats = normalizer(feats, wav_lens)
        emb = xvector_extractor(feats, wav_lens)

        # feats = params["compute_features"](wavs)
        # feats = params["mean_var_norm"](feats, lens)
        # emb = params["embedding_model"](feats, lens)
        emb = emb_normalizer(
            emb, torch.ones(emb.shape[0], device=device)
        )
    return emb

# wavs = audio_pipeline()
signal, fs = torchaudio.load("/media/volume1/aicasr/meta-transfer-asr/tests/774.wav")
x = compute_embeddings(signal)
print(x)
print(x.shape)
