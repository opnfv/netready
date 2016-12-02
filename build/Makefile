GLUON_REPO=https://github.com/openstack/gluon.git
GLUON_BRANCH=master
GLUON_VER=0.0.1
GLUON_TAR=gluon.tar.gz
GLUON_RPM=noarch/gluon-$(GLUON_VER)-1.noarch.rpm

.PHONY: all

all: gluon

.PHONY: gluon
gluon: $(GLUON_RPM)

.PHONY: clean
clean: clean-gluon

.PHONY: clean-gluon
clean-gluon:
	rm -rf BUILDROOT
	rm -rf noarch
	rm -f $(GLUON_TAR)
	rm -f openstack-proton-server.service
	rm -f proton.conf
	rm -rf gluon-$(GLUON_VER)

$(GLUON_TAR):
	@echo cloning Gluon git repo
	git clone $(GLUON_REPO) -b $(GLUON_BRANCH) gluon-$(GLUON_VER)
	tar czf gluon.tar.gz gluon-$(GLUON_VER)

$(GLUON_RPM): $(GLUON_TAR)
	@echo building Gluon RPM
	rpmbuild --clean -bb --target noarch rpm_specs/gluon.spec -D '_topdir %(echo `pwd`)' -D '_builddir %(echo `pwd`)' -D '_sourcedir %(echo `pwd`)' -D %'_rpmdir %(echo `pwd`)' -D '_specdir %(echo `pwd`)' -D '_srcrpmdir %(echo `pwd`)'
