"""
Workload template
04/18/2020 Lin Cheng (lc873@cornell.edu)
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

"""
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import MNIST
from utils import parse_model_args, train, inference, save_model
"""

# -------------------------------------------------------------------------
# Multilayer Preception for MNIST
# -------------------------------------------------------------------------

"""
class MLPModel(nn.Module):

    def __init__(self):
        super(MLPModel, self).__init__()

        self.mnist = nn.Sequential(nn.Linear(784, 128),
                                   nn.ReLU(),
                                   nn.Dropout(0.2),
                                   nn.Linear(128, 64),
                                   nn.ReLU(),
                                   nn.Dropout(0.2),
                                   nn.Linear(64, 10))

    def forward(self, x):
        return self.mnist(x.view(-1, 28 * 28))
"""

# -------------------------------------------------------------------------
# Workload specific command line arguments
# -------------------------------------------------------------------------

"""
def extra_arg_parser(parser):
    parser.add_argument('--lr', default=0.01, type=int,
                        help="learning rate")
"""

if __name__ == "__main__":
    # -------------------------------------------------------------------------
    # Parse command line arguments
    # -------------------------------------------------------------------------

    """
    args = parse_model_args(extra_arg_parser)
    """

    # -------------------------------------------------------------------------
    # Prepare Dataset
    # -------------------------------------------------------------------------

    """
    train_data = MNIST('./data', train=True, download=True,
                       transform=transforms.ToTensor())
    test_data = MNIST('./data', train=False, download=True,
                      transform=transforms.ToTensor())

    train_loader = DataLoader(train_data, batch_size=args.batch_size,
                              num_workers=0)
    test_loader = DataLoader(test_data, batch_size=args.batch_size,
                             num_workers=0)
    """

    # -------------------------------------------------------------------------
    # Model creation and loading
    # -------------------------------------------------------------------------

    """
    LEARNING_RATE = args.lr
    model = MLPModel()

    optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)
    criterion = nn.CrossEntropyLoss()

    # Load pretrained model if necessary
    if args.load_model:
        model.load_state_dict(torch.load(args.model_filename))

    # Move model to HammerBlade if using HB
    if args.hammerblade:
        model.to(torch.device("hammerblade"))

    print(model)

    # Quit here if dry run
    if args.dry:
        exit(0)
    """

    # -------------------------------------------------------------------------
    # Training
    # -------------------------------------------------------------------------

    """
    if args.training:

        train(model,
              train_loader,
              optimizer,
              criterion,
              args)
    """

    # -------------------------------------------------------------------------
    # Inference
    # -------------------------------------------------------------------------

    """
    if args.inference:

        inference(model,
                  test_loader,
                  criterion,
                  args)
    """

    # -------------------------------------------------------------------------
    # Model saving
    # -------------------------------------------------------------------------
    """
    if args.save_model:
        save_model(model, args.model_filename)
    """
