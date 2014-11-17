PLAT= linux
PLATS=linux

all: $(PLAT)

$(PLATS) install local clean:
	$(MAKE) -C src $@

print:
	$(MAKE) -C src $@

test:
	lua test/hello.lua

install:
	@cd src; $(MAKE) $(PLAT) LUAV=5.2
	@cd src; $(MAKE) install LUAV=5.2

.PHONY: test

