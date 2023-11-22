#@title (OPTIONAL) Pick any models you want to use and launch the script to download them 
import os

#@markdown **Choose your Checkpoint model**
model = "Pastel Mix" #@param ["None", "Anything v3.0", "Grapefruit v4.1","AOM3","Pastel Mix"] {allow-input: true}
vae = "kl-f8-anime2" #@param ["None","pastel-waifu-diffusion","kl-f8-anime2","animefull-final (BlueMoonMix)","vae-ft-mse-840000-ema (Good with DisillusionMix)","orangemix"] {allow-input: true}
ti = "None" #@param ["None","EasyNegative"] {allow-input: true}

#This is where all the models and their links are located
if model == "None":
  model_download_url = ""
  model_file_name = ""
elif model == "Anything v3.0":
  model_download_url = "https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/anything-v3-fp16-pruned.safetensors"
  model_file_name = "anything-v3-fp16-pruned.safetensors"
elif model == "Grapefruit v4.1":
  model_download_url = "https://civitai.com/api/download/models/16619"
  model_file_name = "grapefruitHentaiModel_grapefruitv41.safetensors"
elif model == "Pastel Mix":
  model_download_url = "https://huggingface.co/andite/pastel-mix/resolve/main/pastelmix-fp16.safetensors"
  model_file_name = "pastelmix-fp16.safetensors"
elif model == "Andromeda-Mix":
  model_download_url = "https://civitai.com/api/download/models/7671"
  model_file_name = "andromedaMix_andromedaVersion2.safetensors"
elif model == "Cetus-Mix Coda Edition":
  model_download_url = "https://civitai.com/api/download/models/20229"
  model_file_name = "cetusMix_Codaedition.safetensors"
elif model == "Cetus-Mix V3":
  model_download_url = "https://civitai.com/api/download/models/18496"
  model_file_name = "cetusMix_cetusVersion3.safetensors"
elif model == "ColorBomb":
  model_download_url = "https://huggingface.co/mocker/KaBoom/resolve/main/ColorBombMix-fp16-no-ema.safetensors"
  model_file_name = "ColorBombMix-fp16-no-ema.safetensors"
elif model == "FaceBomb":
  model_download_url = "https://huggingface.co/mocker/KaBoom/resolve/main/FaceBombMix-fp16-no-ema.safetensors"
  model_file_name = "FaceBombMix-fp16-no-ema.safetensors"
elif model == "HyperBomb":
  model_download_url = "https://huggingface.co/mocker/KaBoom/resolve/main/HyperBombMix-fp16-no-ema.safetensors"
  model_file_name = "HyperBombMix-fp16-no-ema.safetensors"
elif model == "VividibiMix":
  model_download_url = "https://civitai.com/api/download/models/9644"
  model_file_name = "vividibimix_.safetensors"
elif model == "WhiteSpace Prism":
  model_download_url = "https://civitai.com/api/download/models/15240?type=Pruned%20Model&format=SafeTensor"
  model_file_name = "whitespace_Prism.safetensors"
elif model == "BlueMoonMix":
  model_download_url = "https://civitai.com/api/download/models/23726"
  model_file_name = "bluemoonmix_v1.safetensors"
elif model == "PileDream":
  model_download_url = "https://civitai.com/api/download/models/26119"
  model_file_name = "piledream_.safetensors"
elif model == "Pretty 2D":
  model_download_url = "https://civitai.com/api/download/models/18377"
  model_file_name = "pretty2D_pretty2DPrunedFp16.safetensors"
elif model == "Pretty 2.5D":
  model_download_url = "https://civitai.com/api/download/models/18371"
  model_file_name = "pretty25D_pretty25DPrunedFp16.safetensors"
elif model == "Pretty 2.5D V2":
  model_download_url = "https://civitai.com/api/download/models/20775"
  model_file_name = "pretty25DV2_pretty25DV2Pruned.safetensors"
elif model == "Kawaii 2D":
  model_download_url = "https://civitai.com/api/download/models/22503"
  model_file_name = "kawaii2D_kawaii2DV11Pruend.safetensors"
elif model == "Kawaii 2.5D":
  model_download_url = "https://civitai.com/api/download/models/22509"
  model_file_name = "kawaii25D_kawaii25DV2Pruend.safetensors"
elif model == "Animelike 2D":
  model_download_url = "https://civitai.com/api/download/models/25853"
  model_file_name = "animelike2D_animelike2DPruned.safetensors"
elif model == "Animelike 2.5D":
  model_download_url = "https://civitai.com/api/download/models/26176"
  model_file_name = "animelike25D_animelike25DV11Pruned.safetensors"
elif model == "Beauty 2.5D":
  model_download_url = "https://civitai.com/api/download/models/21564"
  model_file_name = "beauty25D_beauty25DPrunedFp16.safetensors"
elif model == "CreamMix":
  model_download_url = "https://civitai.com/api/download/models/23650"
  model_file_name = "creammix_v10.safetensors"
elif model == "Counterfeit v2.5":
  model_download_url = "https://huggingface.co/gsdf/Counterfeit-V2.5/resolve/main/Counterfeit-V2.5_fp16.safetensors"
  model_file_name = "Counterfeit-V2.5_fp16.safetensors"
elif model == "Counterfeit v2.2":
  model_download_url = "https://huggingface.co/gsdf/Counterfeit-V2.5/resolve/main/Counterfeit-V2.2.safetensors"
  model_file_name = "Counterfeit-V2.2.safetensors"
elif model == "ChilloutMix":
  model_download_url = "https://civitai.com/api/download/models/11732"
  model_file_name = "chilloutmix_NiPrunedFp16Fix.safetensors"
elif model == "refslaveV2_v2 (good for environmental stuff)":
  model_download_url = "https://huggingface.co/Dorshu/refslaveV2_v2/resolve/main/refslaveV2_v2.safetensors"
  model_file_name = "refslaveV2_v2.safetensors"
elif model == "WinterMoonMix A":
  model_download_url = "https://civitai.com/api/download/models/15708"
  model_file_name = "wintermoonmix_A.safetensors"
elif model == "CyriousMix":
  model_download_url = "https://civitai.com/api/download/models/7951"
  model_file_name = "cyriousmix_14.safetensors"
elif model == "KuromiMix V1.0":
  model_download_url = "https://civitai.com/api/download/models/25529"
  model_file_name = "kuromimix_V10.safetensors"
elif model == "KuromiMix V2.0":
  model_download_url = "https://civitai.com/api/download/models/25578"
  model_file_name = "kuromimix_V20.ckpt"
elif model == "MeinaUnreal":
  model_download_url = "https://civitai.com/api/download/models/22314"
  model_file_name = "meinaunreal_v1Beta.safetensors"
elif model == "CamelliaBlossomMix":
  model_download_url = "https://civitai.com/api/download/models/21759"
  model_file_name = "camelliablossommix_finaledition.safetensors"
elif model == "EtherRealMix v1.1":
  model_download_url = "https://civitai.com/api/download/models/23036"
  model_file_name = "etherRealMix_V11.safetensors"
elif model == "DisillusionMix v3":
  model_download_url = "https://civitai.com/api/download/models/21229"
  model_file_name = "disillusionmix_3.safetensors"
elif model == "DisillusionMix v2":
  model_download_url = "https://civitai.com/api/download/models/20544"
  model_file_name = "disillusionmix_2.safetensors"
elif model == "AOM3":
  model_download_url = "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3_orangemixs.safetensors"
  model_file_name = "AOM3_orangemixs.safetensors"
elif model == "AOM3A1":
  model_download_url = "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A1_orangemixs.safetensors"
  model_file_name = "AOM3A1_orangemixs.safetensors"
elif model == "AOM3A1B":
  model_download_url = "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A1B_orangemixs.safetensors"
  model_file_name = "AOM3A1B_orangemixs.safetensors"
elif model == "AOM3A2":
  model_download_url = "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A2_orangemixs.safetensors"
  model_file_name = "AOM3A2_orangemixs.safetensors"
elif model == "AOM3A3":
  model_download_url = "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A3_orangemixs.safetensors"
  model_file_name = "AOM3A3_orangemixs.safetensors"
elif model == "Fish-mix":
  model_download_url = "https://civitai.com/api/download/models/18583"
  model_file_name = "MixFishMix_v10.safetensors"
elif model == "Mechanicmix_V2 (2D)":
  model_download_url = "https://civitai.com/api/download/models/18955"
  model_file_name = "mechanicmixV2_mechanicmixV2.safetensors"
elif model == "Mechanicmix_V1 (2.5D)":
  model_download_url = "https://civitai.com/api/download/models/17532"
  model_file_name = "mechanicmixV2_mechanicmixV1.safetensors"
elif model == "":
  model_download_url = ""
  model_file_name = ""

#This is where all the vae and their links are located
if vae == "None":
  vae_download_url = ""
  vae_file_name = ""
elif vae == "pastel-waifu-diffusion":
  vae_download_url = "https://huggingface.co/andite/pastel-mix/resolve/main/pastel-waifu-diffusion.vae.pt"
  vae_file_name = "pastel-waifu-diffusion.vae.pt"
elif vae == "kl-f8-anime2":
  vae_download_url = "https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime2.ckpt"
  vae_file_name = "kl-f8-anime2.ckpt"
elif vae == "animefull-final (BlueMoonMix)":
  vae_download_url = "https://civitai.com/api/download/models/23726?type=VAE&format=Other"
  vae_file_name = "animefull-final-pruned.vae.pt"
elif vae == "vae-ft-mse-840000-ema (Good with DisillusionMix)":
  vae_download_url = "https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors"
  vae_file_name = "vae-ft-mse-840000-ema-pruned.safetensors"
elif vae == "orangemix":
  vae_download_url = "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/VAEs/orangemix.vae.pt"
  vae_file_name = "orangemix.vae.pt"
elif vae == "":
  vae_download_url = ""
  vae_file_name = ""

#This is where Textual Inversions and their links are located
if ti == "None":
  ti_download_url = ""
  ti_file_name = ""
elif ti == "EasyNegative":
  ti_download_url = "https://huggingface.co/datasets/gsdf/EasyNegative/resolve/main/EasyNegative.safetensors"
  ti_file_name = "EasyNegative.safetensors"


#Download everything
if model != "None":
  model_download = "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {} -d {} -o {}".format(model_download_url, models_path, model_file_name)
else:
  print("No model selected for download. Skipping...")

if vae != "None":
  vae_download = "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {} -d {} -o {}".format(vae_download_url, vae_path, vae_file_name)
else:
  print("No vae selected for download. Skipping...")

if ti !="None":
  ti_download = "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {} -d {} -o {}".format(ti_download_url, ti_path, ti_file_name)
else:
  print("No textual inversion selected for download. Skipping...")

!{model_download}
!{vae_download}
!{ti_download}