# config #######################################################################
name                 = python_for_datascience
need_sudo            = true
docker_start_folder  = ../src

# colors #######################################################################
gray                 = \033[0;30m
red                  = \033[0;31m
green                = \033[0;32m
yellow               = \033[1;33m
blue                 = \033[0;34m
magenta              = \033[0;35m
cyan                 = \033[0;36m
reset                = \033[0m
main_color           = $(blue)
tag                  = "[ $(main_color)$(name)$(reset) ]"

# options ######################################################################
keep_on_error        = || true

# commands #####################################################################
docker-compose       = $(if $(filter $(need_sudo),true),\
                           $(shell which sudo) $(shell which docker-compose),\
                           $(shell which docker-compose)\
                        )
echo                 = $$(which echo) -e $(tag)
make                 = $$(which make) --quiet
sudo                 = $$(which sudo)

# special targets ##############################################################
.PHONY               : all clean fclean re
.PHONY               : build up down stop enter
.PHONY               : sudo duck

# basic rules ##################################################################
all:
	@$(echo) "make all"
	@$(make) down
	@$(make) up_detach
	@$(make) enter
	@$(echo) "make all done."

clean:
	@$(echo) "make clean"
	@$(make) stop
	@$(echo) "make clean done."

fclean:
	@$(echo) "make fclean"
	@$(make) clean
	@$(make) down
	@$(echo) "make fclean done."

re:
	@$(echo) "make re"
	@$(make) fclean
	@$(make) all
	@$(echo) "make re done."

# docker rules #################################################################
build: sudo
	@$(echo) "Building $(name) container..."
	@$(docker-compose) build
	@$(echo) "$(name) container built."

up_detach: sudo
	@$(echo) "Starting $(name) container..."
	@$(make) build
	@$(docker-compose) up --detach
	@$(echo) "$(name) container started."

down: sudo
	@$(echo) "Stopping $(name) container..."
	@$(docker-compose) down
	@$(echo) "$(name) container stopped."

stop: sudo
	@$(echo) "Stopping $(name) container..."
	@$(docker-compose) stop
	@$(echo) "$(name) container stopped."

enter: sudo
	@$(echo) "Entering $(name) container..."
	@$(docker-compose) exec $(name) bash \
		-c "cd $(docker_start_folder) && echo 'alias norminette=flake8' >> ~/.bashrc && exec bash"
	@$(echo) "Exited $(name) container."

# tools rules ##################################################################
sudo:
	@$(echo) "Requesting sudo..."
	@$(sudo) true
	@$(echo) "Sudo granted."

duck:
	@$(echo) "Furious Quacking Sound Effect"
