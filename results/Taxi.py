import gym

from DDQN import DDQN
from HRL import HRL
from SAC_Discrete import SAC_Discrete
from hierarchical_agents.SNN_HRL import SNN_HRL
from agents.Trainer import Trainer
from utilities.data_structures.Config import Config
from agents.DQN_agents.DQN import DQN
from agents.hierarchical_agents.h_DQN import h_DQN

config = Config()
config.seed = 1
config.environment = gym.make("Taxi-v2")
config.env_parameters = {}
config.num_episodes_to_run = 500
config.file_to_save_data_results = "data_and_graphs/hrl_experiments/Cart_Pole_data.pkl"
config.file_to_save_results_graph = "data_and_graphs/hrl_experiments/Cart_Pole.png"
config.show_solution_score = False
config.visualise_individual_results = False
config.visualise_overall_agent_results = True
config.standard_deviation_results = 1.0
config.runs_per_agent = 3
config.use_GPU = False
config.overwrite_existing_results_file = False
config.randomise_random_seed = True
config.save_model = False


linear_hidden_units = [32, 32]
learning_rate = 0.001
buffer_size = 100000
batch_size = 256
batch_norm = False
embedding_dimensionality = 10
gradient_clipping_norm = 0.7  #needs to be optimised
update_every_n_steps = 1
learning_iterations = 1
epsilon_decay_rate_denominator = 5 #150
min_num_episodes_to_play = 20 #80
discount_rate = 0.99
tau = 0.01
sequitur_k = 2
pre_training_learning_iterations_multiplier = 500
episodes_to_run_with_no_exploration = 0
action_balanced_replay_buffer = True
copy_over_hidden_layers = True

num_top_results_to_use = 10
action_frequency_required_in_top_results = 1.0

random_episodes_to_run = 0

action_length_reward_bonus = 0.05
use_global_list_of_best_performing_actions = True

only_train_new_actions = True
only_train_final_layer = True
reduce_macro_action_appearance_cutoff_throughout_training = False
add_1_macro_action_at_a_time = True

calculate_q_values_as_increments = True
increase_batch_size_with_actions = False
abandon_ship = True
clip_rewards = False


config.debug_mode = False

config.hyperparameters = {

    "HRL": {
        "linear_hidden_units": linear_hidden_units,
        "learning_rate": learning_rate,
        "buffer_size": buffer_size,
        "batch_size": batch_size,
        "final_layer_activation": "None",
        "columns_of_data_to_be_embedded": [0],
        "embedding_dimensions": [[config.environment.observation_space.n, embedding_dimensionality]],
        "batch_norm": batch_norm,
        "gradient_clipping_norm": gradient_clipping_norm,
        "update_every_n_steps": update_every_n_steps,
        "epsilon_decay_rate_denominator": epsilon_decay_rate_denominator,
        "discount_rate": discount_rate,
        "learning_iterations": learning_iterations,
        "tau": tau,
        "sequitur_k": sequitur_k,
        "action_length_reward_bonus": action_length_reward_bonus,
        "pre_training_learning_iterations_multiplier": pre_training_learning_iterations_multiplier,
        "episodes_to_run_with_no_exploration": episodes_to_run_with_no_exploration,
        "action_balanced_replay_buffer": action_balanced_replay_buffer,
        "copy_over_hidden_layers": copy_over_hidden_layers,
        "use_global_list_of_best_performing_actions": use_global_list_of_best_performing_actions,
        "random_episodes_to_run": random_episodes_to_run,
        "only_train_new_actions": only_train_new_actions,
        "only_train_final_layer": only_train_final_layer,
        "num_top_results_to_use": num_top_results_to_use,
        "action_frequency_required_in_top_results": action_frequency_required_in_top_results,
        "reduce_macro_action_appearance_cutoff_throughout_training": reduce_macro_action_appearance_cutoff_throughout_training,
        "add_1_macro_action_at_a_time": add_1_macro_action_at_a_time,
        "calculate_q_values_as_increments": calculate_q_values_as_increments,
        "min_num_episodes_to_play": min_num_episodes_to_play,
        "increase_batch_size_with_actions": increase_batch_size_with_actions,
        "abandon_ship": abandon_ship,
        "clip_rewards": clip_rewards
    },

    "DQN_Agents": {
        "linear_hidden_units": linear_hidden_units,
        "learning_rate": learning_rate,
        "buffer_size": buffer_size,
        "batch_size": batch_size,
        "final_layer_activation": "None",
        # "columns_of_data_to_be_embedded": [0],
        # "embedding_dimensions": [[config.environment.observation_space.n, embedding_dimensionality]],
        "batch_norm": batch_norm,
        "gradient_clipping_norm": gradient_clipping_norm,
        "update_every_n_steps": update_every_n_steps,
        "epsilon_decay_rate_denominator": epsilon_decay_rate_denominator,
        "discount_rate": discount_rate,
        "learning_iterations": learning_iterations,
        "tau": tau,
        "clip_rewards": clip_rewards
    },

    "Actor_Critic_Agents": {
        "Actor": {
            "learning_rate": 0.0003,
            "linear_hidden_units": [64, 64],
            "final_layer_activation": "Softmax",
            # "columns_of_data_to_be_embedded": [0],
            # "embedding_dimensions": [[config.environment.observation_space.n, embedding_dimensionality]],
            "batch_norm": False,
            "tau": 0.005,
            "gradient_clipping_norm": 5,
            "initialiser": "Xavier"
        },

        "Critic": {
            "learning_rate": 0.0003,
            "linear_hidden_units": [64, 64],
            "final_layer_activation": None,
            # "columns_of_data_to_be_embedded": [0],
            # "embedding_dimensions": [[config.environment.observation_space.n, embedding_dimensionality]],
            "batch_norm": False,
            "buffer_size": 1000000,
            "tau": 0.005,
            "gradient_clipping_norm": 5,
            "initialiser": "Xavier"
        },

        "min_steps_before_learning": 10000,
        "batch_size": 256,
        "discount_rate": 0.99,
        "mu": 0.0,  # for O-H noise
        "theta": 0.15,  # for O-H noise
        "sigma": 0.25,  # for O-H noise
        "action_noise_std": 0.2,  # for TD3
        "action_noise_clipping_range": 0.5,  # for TD3
        "update_every_n_steps": 1,
        "learning_updates_per_learning_session": 1,
        "automatically_tune_entropy_hyperparameter": True,
        "entropy_term_weight": None,
        "add_extra_noise": False,
        "do_evaluation_iterations": True,
        "clip_rewards": clip_rewards
    }
}


if __name__ == "__main__":
    AGENTS = [ HRL] #  DDQN] #, SAC_Discrete,  SAC_Discrete, DDQN] #HRL] #, SNN_HRL, DQN, h_DQN]
    trainer = Trainer(config, AGENTS)
    trainer.run_games_for_agents()



