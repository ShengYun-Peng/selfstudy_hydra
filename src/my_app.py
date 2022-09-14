from omegaconf import DictConfig, OmegaConf
import hydra
import logging

# logger
log = logging.getLogger(__name__)

@hydra.main(config_path="../configs", config_name="config", version_base="1.2")
def my_app(cfg: DictConfig) -> None:
    # print(OmegaConf.to_yaml(cfg))
    log.info("Info level message")
    log.info(OmegaConf.to_yaml(cfg))
    log.debug("Debug level message")

if __name__ == "__main__":
    my_app()