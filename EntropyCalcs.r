library(vcd)
library(entropy)
library(parmigene)

templates = read.csv('/Users/jcgood/gitrepos/desmeme/EntropyTables.txt', header=TRUE, row.names=1)

violability = table(templates$violability)
names(dimnames(violability)) <- list('violability')
Hviolability = entropy(violability)

conditioning = table(templates$conditioning)
names(dimnames(conditioning)) <- list('conditioning')
Hconditioning = entropy(conditioning)

exceptionality = table(templates$exceptionality)
names(dimnames(exceptionality)) <- list('exceptionality')
Hexceptionality = entropy(exceptionality)

reparability = table(templates$reparability)
names(dimnames(reparability)) <- list('reparability')
Hreparability = entropy(reparability)

foundation = table(templates$foundation)
names(dimnames(foundation)) <- list('foundation')
Hfoundation = entropy(foundation)

stricture = table(templates$stricture)
names(dimnames(stricture)) <- list('stricture')
Hstricture = entropy(stricture)

relations = table(templates$relations)
names(dimnames(relations)) <- list('relations')
Hrelations = entropy(relations)

constituent = table(templates$constituent)
names(dimnames(constituent)) <- list('constituent')
Hconstituent = entropy(constituent)

count = table(templates$count)
names(dimnames(count)) <- list('count')
Hcount = entropy(count)

violabilityviolabilityMI = 0

violabilityconditioning = table(templates$violability,templates$conditioning)
names(dimnames(violabilityconditioning)) <- list('violability','conditioning')
violabilityconditioningMI = mi.shrink(violabilityconditioning)

violabilityexceptionality = table(templates$violability,templates$exceptionality)
names(dimnames(violabilityexceptionality)) <- list('violability','exceptionality')
violabilityexceptionalityMI = mi.shrink(violabilityexceptionality)

violabilityreparability = table(templates$violability,templates$reparability)
names(dimnames(violabilityreparability)) <- list('violability','reparability')
violabilityreparabilityMI = mi.shrink(violabilityreparability)

violabilityfoundation = table(templates$violability,templates$foundation)
names(dimnames(violabilityfoundation)) <- list('violability','foundation')
violabilityfoundationMI = mi.shrink(violabilityfoundation)

violabilitystricture = table(templates$violability,templates$stricture)
names(dimnames(violabilitystricture)) <- list('violability','stricture')
violabilitystrictureMI = mi.shrink(violabilitystricture)

violabilityrelations = table(templates$violability,templates$relations)
names(dimnames(violabilityrelations)) <- list('violability','relations')
violabilityrelationsMI = mi.shrink(violabilityrelations)

violabilityconstituent = table(templates$violability,templates$constituent)
names(dimnames(violabilityconstituent)) <- list('violability','constituent')
violabilityconstituentMI = mi.shrink(violabilityconstituent)

violabilitycount = table(templates$violability,templates$count)
names(dimnames(violabilitycount)) <- list('violability','count')
violabilitycountMI = mi.shrink(violabilitycount)


conditioningviolability = violabilityconditioning
conditioningviolabilityMI = violabilityconditioningMI

conditioningconditioningMI = 0

conditioningexceptionality = table(templates$conditioning,templates$exceptionality)
names(dimnames(conditioningexceptionality)) <- list('conditioning','exceptionality')
conditioningexceptionalityMI = mi.shrink(conditioningexceptionality)

conditioningreparability = table(templates$conditioning,templates$reparability)
names(dimnames(conditioningreparability)) <- list('conditioning','reparability')
conditioningreparabilityMI = mi.shrink(conditioningreparability)

conditioningfoundation = table(templates$conditioning,templates$foundation)
names(dimnames(conditioningfoundation)) <- list('conditioning','foundation')
conditioningfoundationMI = mi.shrink(conditioningfoundation)

conditioningstricture = table(templates$conditioning,templates$stricture)
names(dimnames(conditioningstricture)) <- list('conditioning','stricture')
conditioningstrictureMI = mi.shrink(conditioningstricture)

conditioningrelations = table(templates$conditioning,templates$relations)
names(dimnames(conditioningrelations)) <- list('conditioning','relations')
conditioningrelationsMI = mi.shrink(conditioningrelations)

conditioningconstituent = table(templates$conditioning,templates$constituent)
names(dimnames(conditioningconstituent)) <- list('conditioning','constituent')
conditioningconstituentMI = mi.shrink(conditioningconstituent)

conditioningcount = table(templates$conditioning,templates$count)
names(dimnames(conditioningcount)) <- list('conditioning','count')
conditioningcountMI = mi.shrink(conditioningcount)


exceptionalityviolability = violabilityexceptionality
exceptionalityviolabilityMI = violabilityexceptionalityMI

exceptionalityconditioning = conditioningexceptionality
exceptionalityconditioningMI = conditioningexceptionalityMI

exceptionalityexceptionalityMI = 0

exceptionalityreparability = table(templates$exceptionality,templates$reparability)
names(dimnames(exceptionalityreparability)) <- list('exceptionality','reparability')
exceptionalityreparabilityMI = mi.shrink(exceptionalityreparability)

exceptionalityfoundation = table(templates$exceptionality,templates$foundation)
names(dimnames(exceptionalityfoundation)) <- list('exceptionality','foundation')
exceptionalityfoundationMI = mi.shrink(exceptionalityfoundation)

exceptionalitystricture = table(templates$exceptionality,templates$stricture)
names(dimnames(exceptionalitystricture)) <- list('exceptionality','stricture')
exceptionalitystrictureMI = mi.shrink(exceptionalitystricture)

exceptionalityrelations = table(templates$exceptionality,templates$relations)
names(dimnames(exceptionalityrelations)) <- list('exceptionality','relations')
exceptionalityrelationsMI = mi.shrink(exceptionalityrelations)

exceptionalityconstituent = table(templates$exceptionality,templates$constituent)
names(dimnames(exceptionalityconstituent)) <- list('exceptionality','constituent')
exceptionalityconstituentMI = mi.shrink(exceptionalityconstituent)

exceptionalitycount = table(templates$exceptionality,templates$count)
names(dimnames(exceptionalitycount)) <- list('exceptionality','count')
exceptionalitycountMI = mi.shrink(exceptionalitycount)


reparabilityviolability = violabilityreparability
reparabilityviolabilityMI = violabilityreparabilityMI

reparabilityconditioning = conditioningreparability
reparabilityconditioningMI = conditioningreparabilityMI

reparabilityexceptionality = exceptionalityreparability
reparabilityexceptionalityMI = exceptionalityreparabilityMI

reparabilityreparabilityMI = 0

reparabilityfoundation = table(templates$reparability,templates$foundation)
names(dimnames(reparabilityfoundation)) <- list('reparability','foundation')
reparabilityfoundationMI = mi.shrink(reparabilityfoundation)

reparabilitystricture = table(templates$reparability,templates$stricture)
names(dimnames(reparabilitystricture)) <- list('reparability','stricture')
reparabilitystrictureMI = mi.shrink(reparabilitystricture)

reparabilityrelations = table(templates$reparability,templates$relations)
names(dimnames(reparabilityrelations)) <- list('reparability','relations')
reparabilityrelationsMI = mi.shrink(reparabilityrelations)

reparabilityconstituent = table(templates$reparability,templates$constituent)
names(dimnames(reparabilityconstituent)) <- list('reparability','constituent')
reparabilityconstituentMI = mi.shrink(reparabilityconstituent)

reparabilitycount = table(templates$reparability,templates$count)
names(dimnames(reparabilitycount)) <- list('reparability','count')
reparabilitycountMI = mi.shrink(reparabilitycount)


foundationviolability = violabilityfoundation
foundationviolabilityMI = violabilityfoundationMI

foundationconditioning = conditioningfoundation
foundationconditioningMI = conditioningfoundationMI

foundationexceptionality = exceptionalityfoundation
foundationexceptionalityMI = exceptionalityfoundationMI

foundationreparability = reparabilityfoundation
foundationreparabilityMI = reparabilityfoundationMI

foundationfoundationMI = 0

foundationstricture = table(templates$foundation,templates$stricture)
names(dimnames(foundationstricture)) <- list('foundation','stricture')
foundationstrictureMI = mi.shrink(foundationstricture)

foundationrelations = table(templates$foundation,templates$relations)
names(dimnames(foundationrelations)) <- list('foundation','relations')
foundationrelationsMI = mi.shrink(foundationrelations)

foundationconstituent = table(templates$foundation,templates$constituent)
names(dimnames(foundationconstituent)) <- list('foundation','constituent')
foundationconstituentMI = mi.shrink(foundationconstituent)

foundationcount = table(templates$foundation,templates$count)
names(dimnames(foundationcount)) <- list('foundation','count')
foundationcountMI = mi.shrink(foundationcount)


strictureviolability = violabilitystricture
strictureviolabilityMI = violabilitystrictureMI

strictureconditioning = conditioningstricture
strictureconditioningMI = conditioningstrictureMI

strictureexceptionality = exceptionalitystricture
strictureexceptionalityMI = exceptionalitystrictureMI

stricturereparability = reparabilitystricture
stricturereparabilityMI = reparabilitystrictureMI

stricturefoundation = foundationstricture
stricturefoundationMI = foundationstrictureMI

stricturestrictureMI = 0

stricturerelations = table(templates$stricture,templates$relations)
names(dimnames(stricturerelations)) <- list('stricture','relations')
stricturerelationsMI = mi.shrink(stricturerelations)

strictureconstituent = table(templates$stricture,templates$constituent)
names(dimnames(strictureconstituent)) <- list('stricture','constituent')
strictureconstituentMI = mi.shrink(strictureconstituent)

stricturecount = table(templates$stricture,templates$count)
names(dimnames(stricturecount)) <- list('stricture','count')
stricturecountMI = mi.shrink(stricturecount)


relationsviolability = violabilityrelations
relationsviolabilityMI = violabilityrelationsMI

relationsconditioning = conditioningrelations
relationsconditioningMI = conditioningrelationsMI

relationsexceptionality = exceptionalityrelations
relationsexceptionalityMI = exceptionalityrelationsMI

relationsreparability = reparabilityrelations
relationsreparabilityMI = reparabilityrelationsMI

relationsfoundation = foundationrelations
relationsfoundationMI = foundationrelationsMI

relationsstricture = stricturerelations
relationsstrictureMI = stricturerelationsMI

relationsrelationsMI = 0

relationsconstituent = table(templates$relations,templates$constituent)
names(dimnames(relationsconstituent)) <- list('relations','constituent')
relationsconstituentMI = mi.shrink(relationsconstituent)

relationscount = table(templates$relations,templates$count)
names(dimnames(relationscount)) <- list('relations','count')
relationscountMI = mi.shrink(relationscount)


constituentviolability = violabilityconstituent
constituentviolabilityMI = violabilityconstituentMI

constituentconditioning = conditioningconstituent
constituentconditioningMI = conditioningconstituentMI

constituentexceptionality = exceptionalityconstituent
constituentexceptionalityMI = exceptionalityconstituentMI

constituentreparability = reparabilityconstituent
constituentreparabilityMI = reparabilityconstituentMI

constituentfoundation = foundationconstituent
constituentfoundationMI = foundationconstituentMI

constituentstricture = strictureconstituent
constituentstrictureMI = strictureconstituentMI

constituentrelations = relationsconstituent
constituentrelationsMI = relationsconstituentMI

constituentconstituentMI = 0

constituentcount = table(templates$constituent,templates$count)
names(dimnames(constituentcount)) <- list('constituent','count')
constituentcountMI = mi.shrink(constituentcount)


countviolability = violabilitycount
countviolabilityMI = violabilitycountMI

countconditioning = conditioningcount
countconditioningMI = conditioningcountMI

countexceptionality = exceptionalitycount
countexceptionalityMI = exceptionalitycountMI

countreparability = reparabilitycount
countreparabilityMI = reparabilitycountMI

countfoundation = foundationcount
countfoundationMI = foundationcountMI

countstricture = stricturecount
countstrictureMI = stricturecountMI

countrelations = relationscount
countrelationsMI = relationscountMI

countconstituent = constituentcount
countconstituentMI = constituentcountMI

countcountMI = 0


Pviolabilityviolability = violabilityviolabilityMI[1] / Hviolability
Pviolabilityviolability = violabilityviolabilityMI[1] / Hviolability

Pviolabilityconditioning = violabilityconditioningMI[1] / Hviolability
Pconditioningviolability = violabilityconditioningMI[1] / Hconditioning

Pviolabilityexceptionality = violabilityexceptionalityMI[1] / Hviolability
Pexceptionalityviolability = violabilityexceptionalityMI[1] / Hexceptionality

Pviolabilityreparability = violabilityreparabilityMI[1] / Hviolability
Preparabilityviolability = violabilityreparabilityMI[1] / Hreparability

Pviolabilityfoundation = violabilityfoundationMI[1] / Hviolability
Pfoundationviolability = violabilityfoundationMI[1] / Hfoundation

Pviolabilitystricture = violabilitystrictureMI[1] / Hviolability
Pstrictureviolability = violabilitystrictureMI[1] / Hstricture

Pviolabilityrelations = violabilityrelationsMI[1] / Hviolability
Prelationsviolability = violabilityrelationsMI[1] / Hrelations

Pviolabilityconstituent = violabilityconstituentMI[1] / Hviolability
Pconstituentviolability = violabilityconstituentMI[1] / Hconstituent

Pviolabilitycount = violabilitycountMI[1] / Hviolability
Pcountviolability = violabilitycountMI[1] / Hcount

Pconditioningviolability = conditioningviolabilityMI[1] / Hconditioning
Pviolabilityconditioning = conditioningviolabilityMI[1] / Hviolability

Pconditioningconditioning = conditioningconditioningMI[1] / Hconditioning
Pconditioningconditioning = conditioningconditioningMI[1] / Hconditioning

Pconditioningexceptionality = conditioningexceptionalityMI[1] / Hconditioning
Pexceptionalityconditioning = conditioningexceptionalityMI[1] / Hexceptionality

Pconditioningreparability = conditioningreparabilityMI[1] / Hconditioning
Preparabilityconditioning = conditioningreparabilityMI[1] / Hreparability

Pconditioningfoundation = conditioningfoundationMI[1] / Hconditioning
Pfoundationconditioning = conditioningfoundationMI[1] / Hfoundation

Pconditioningstricture = conditioningstrictureMI[1] / Hconditioning
Pstrictureconditioning = conditioningstrictureMI[1] / Hstricture

Pconditioningrelations = conditioningrelationsMI[1] / Hconditioning
Prelationsconditioning = conditioningrelationsMI[1] / Hrelations

Pconditioningconstituent = conditioningconstituentMI[1] / Hconditioning
Pconstituentconditioning = conditioningconstituentMI[1] / Hconstituent

Pconditioningcount = conditioningcountMI[1] / Hconditioning
Pcountconditioning = conditioningcountMI[1] / Hcount

Pexceptionalityviolability = exceptionalityviolabilityMI[1] / Hexceptionality
Pviolabilityexceptionality = exceptionalityviolabilityMI[1] / Hviolability

Pexceptionalityconditioning = exceptionalityconditioningMI[1] / Hexceptionality
Pconditioningexceptionality = exceptionalityconditioningMI[1] / Hconditioning

Pexceptionalityexceptionality = exceptionalityexceptionalityMI[1] / Hexceptionality
Pexceptionalityexceptionality = exceptionalityexceptionalityMI[1] / Hexceptionality

Pexceptionalityreparability = exceptionalityreparabilityMI[1] / Hexceptionality
Preparabilityexceptionality = exceptionalityreparabilityMI[1] / Hreparability

Pexceptionalityfoundation = exceptionalityfoundationMI[1] / Hexceptionality
Pfoundationexceptionality = exceptionalityfoundationMI[1] / Hfoundation

Pexceptionalitystricture = exceptionalitystrictureMI[1] / Hexceptionality
Pstrictureexceptionality = exceptionalitystrictureMI[1] / Hstricture

Pexceptionalityrelations = exceptionalityrelationsMI[1] / Hexceptionality
Prelationsexceptionality = exceptionalityrelationsMI[1] / Hrelations

Pexceptionalityconstituent = exceptionalityconstituentMI[1] / Hexceptionality
Pconstituentexceptionality = exceptionalityconstituentMI[1] / Hconstituent

Pexceptionalitycount = exceptionalitycountMI[1] / Hexceptionality
Pcountexceptionality = exceptionalitycountMI[1] / Hcount

Preparabilityviolability = reparabilityviolabilityMI[1] / Hreparability
Pviolabilityreparability = reparabilityviolabilityMI[1] / Hviolability

Preparabilityconditioning = reparabilityconditioningMI[1] / Hreparability
Pconditioningreparability = reparabilityconditioningMI[1] / Hconditioning

Preparabilityexceptionality = reparabilityexceptionalityMI[1] / Hreparability
Pexceptionalityreparability = reparabilityexceptionalityMI[1] / Hexceptionality

Preparabilityreparability = reparabilityreparabilityMI[1] / Hreparability
Preparabilityreparability = reparabilityreparabilityMI[1] / Hreparability

Preparabilityfoundation = reparabilityfoundationMI[1] / Hreparability
Pfoundationreparability = reparabilityfoundationMI[1] / Hfoundation

Preparabilitystricture = reparabilitystrictureMI[1] / Hreparability
Pstricturereparability = reparabilitystrictureMI[1] / Hstricture

Preparabilityrelations = reparabilityrelationsMI[1] / Hreparability
Prelationsreparability = reparabilityrelationsMI[1] / Hrelations

Preparabilityconstituent = reparabilityconstituentMI[1] / Hreparability
Pconstituentreparability = reparabilityconstituentMI[1] / Hconstituent

Preparabilitycount = reparabilitycountMI[1] / Hreparability
Pcountreparability = reparabilitycountMI[1] / Hcount

Pfoundationviolability = foundationviolabilityMI[1] / Hfoundation
Pviolabilityfoundation = foundationviolabilityMI[1] / Hviolability

Pfoundationconditioning = foundationconditioningMI[1] / Hfoundation
Pconditioningfoundation = foundationconditioningMI[1] / Hconditioning

Pfoundationexceptionality = foundationexceptionalityMI[1] / Hfoundation
Pexceptionalityfoundation = foundationexceptionalityMI[1] / Hexceptionality

Pfoundationreparability = foundationreparabilityMI[1] / Hfoundation
Preparabilityfoundation = foundationreparabilityMI[1] / Hreparability

Pfoundationfoundation = foundationfoundationMI[1] / Hfoundation
Pfoundationfoundation = foundationfoundationMI[1] / Hfoundation

Pfoundationstricture = foundationstrictureMI[1] / Hfoundation
Pstricturefoundation = foundationstrictureMI[1] / Hstricture

Pfoundationrelations = foundationrelationsMI[1] / Hfoundation
Prelationsfoundation = foundationrelationsMI[1] / Hrelations

Pfoundationconstituent = foundationconstituentMI[1] / Hfoundation
Pconstituentfoundation = foundationconstituentMI[1] / Hconstituent

Pfoundationcount = foundationcountMI[1] / Hfoundation
Pcountfoundation = foundationcountMI[1] / Hcount

Pstrictureviolability = strictureviolabilityMI[1] / Hstricture
Pviolabilitystricture = strictureviolabilityMI[1] / Hviolability

Pstrictureconditioning = strictureconditioningMI[1] / Hstricture
Pconditioningstricture = strictureconditioningMI[1] / Hconditioning

Pstrictureexceptionality = strictureexceptionalityMI[1] / Hstricture
Pexceptionalitystricture = strictureexceptionalityMI[1] / Hexceptionality

Pstricturereparability = stricturereparabilityMI[1] / Hstricture
Preparabilitystricture = stricturereparabilityMI[1] / Hreparability

Pstricturefoundation = stricturefoundationMI[1] / Hstricture
Pfoundationstricture = stricturefoundationMI[1] / Hfoundation

Pstricturestricture = stricturestrictureMI[1] / Hstricture
Pstricturestricture = stricturestrictureMI[1] / Hstricture

Pstricturerelations = stricturerelationsMI[1] / Hstricture
Prelationsstricture = stricturerelationsMI[1] / Hrelations

Pstrictureconstituent = strictureconstituentMI[1] / Hstricture
Pconstituentstricture = strictureconstituentMI[1] / Hconstituent

Pstricturecount = stricturecountMI[1] / Hstricture
Pcountstricture = stricturecountMI[1] / Hcount

Prelationsviolability = relationsviolabilityMI[1] / Hrelations
Pviolabilityrelations = relationsviolabilityMI[1] / Hviolability

Prelationsconditioning = relationsconditioningMI[1] / Hrelations
Pconditioningrelations = relationsconditioningMI[1] / Hconditioning

Prelationsexceptionality = relationsexceptionalityMI[1] / Hrelations
Pexceptionalityrelations = relationsexceptionalityMI[1] / Hexceptionality

Prelationsreparability = relationsreparabilityMI[1] / Hrelations
Preparabilityrelations = relationsreparabilityMI[1] / Hreparability

Prelationsfoundation = relationsfoundationMI[1] / Hrelations
Pfoundationrelations = relationsfoundationMI[1] / Hfoundation

Prelationsstricture = relationsstrictureMI[1] / Hrelations
Pstricturerelations = relationsstrictureMI[1] / Hstricture

Prelationsrelations = relationsrelationsMI[1] / Hrelations
Prelationsrelations = relationsrelationsMI[1] / Hrelations

Prelationsconstituent = relationsconstituentMI[1] / Hrelations
Pconstituentrelations = relationsconstituentMI[1] / Hconstituent

Prelationscount = relationscountMI[1] / Hrelations
Pcountrelations = relationscountMI[1] / Hcount

Pconstituentviolability = constituentviolabilityMI[1] / Hconstituent
Pviolabilityconstituent = constituentviolabilityMI[1] / Hviolability

Pconstituentconditioning = constituentconditioningMI[1] / Hconstituent
Pconditioningconstituent = constituentconditioningMI[1] / Hconditioning

Pconstituentexceptionality = constituentexceptionalityMI[1] / Hconstituent
Pexceptionalityconstituent = constituentexceptionalityMI[1] / Hexceptionality

Pconstituentreparability = constituentreparabilityMI[1] / Hconstituent
Preparabilityconstituent = constituentreparabilityMI[1] / Hreparability

Pconstituentfoundation = constituentfoundationMI[1] / Hconstituent
Pfoundationconstituent = constituentfoundationMI[1] / Hfoundation

Pconstituentstricture = constituentstrictureMI[1] / Hconstituent
Pstrictureconstituent = constituentstrictureMI[1] / Hstricture

Pconstituentrelations = constituentrelationsMI[1] / Hconstituent
Prelationsconstituent = constituentrelationsMI[1] / Hrelations

Pconstituentconstituent = constituentconstituentMI[1] / Hconstituent
Pconstituentconstituent = constituentconstituentMI[1] / Hconstituent

Pconstituentcount = constituentcountMI[1] / Hconstituent
Pcountconstituent = constituentcountMI[1] / Hcount

Pcountviolability = countviolabilityMI[1] / Hcount
Pviolabilitycount = countviolabilityMI[1] / Hviolability

Pcountconditioning = countconditioningMI[1] / Hcount
Pconditioningcount = countconditioningMI[1] / Hconditioning

Pcountexceptionality = countexceptionalityMI[1] / Hcount
Pexceptionalitycount = countexceptionalityMI[1] / Hexceptionality

Pcountreparability = countreparabilityMI[1] / Hcount
Preparabilitycount = countreparabilityMI[1] / Hreparability

Pcountfoundation = countfoundationMI[1] / Hcount
Pfoundationcount = countfoundationMI[1] / Hfoundation

Pcountstricture = countstrictureMI[1] / Hcount
Pstricturecount = countstrictureMI[1] / Hstricture

Pcountrelations = countrelationsMI[1] / Hcount
Prelationscount = countrelationsMI[1] / Hrelations

Pcountconstituent = countconstituentMI[1] / Hcount
Pconstituentcount = countconstituentMI[1] / Hconstituent

Pcountcount = countcountMI[1] / Hcount
Pcountcount = countcountMI[1] / Hcount

violabilityRow = c(violabilityviolabilityMI, violabilityconditioningMI, violabilityexceptionalityMI, violabilityreparabilityMI, violabilityfoundationMI, violabilitystrictureMI, violabilityrelationsMI, violabilityconstituentMI, violabilitycountMI)
conditioningRow = c(conditioningviolabilityMI, conditioningconditioningMI, conditioningexceptionalityMI, conditioningreparabilityMI, conditioningfoundationMI, conditioningstrictureMI, conditioningrelationsMI, conditioningconstituentMI, conditioningcountMI)
exceptionalityRow = c(exceptionalityviolabilityMI, exceptionalityconditioningMI, exceptionalityexceptionalityMI, exceptionalityreparabilityMI, exceptionalityfoundationMI, exceptionalitystrictureMI, exceptionalityrelationsMI, exceptionalityconstituentMI, exceptionalitycountMI)
reparabilityRow = c(reparabilityviolabilityMI, reparabilityconditioningMI, reparabilityexceptionalityMI, reparabilityreparabilityMI, reparabilityfoundationMI, reparabilitystrictureMI, reparabilityrelationsMI, reparabilityconstituentMI, reparabilitycountMI)
foundationRow = c(foundationviolabilityMI, foundationconditioningMI, foundationexceptionalityMI, foundationreparabilityMI, foundationfoundationMI, foundationstrictureMI, foundationrelationsMI, foundationconstituentMI, foundationcountMI)
strictureRow = c(strictureviolabilityMI, strictureconditioningMI, strictureexceptionalityMI, stricturereparabilityMI, stricturefoundationMI, stricturestrictureMI, stricturerelationsMI, strictureconstituentMI, stricturecountMI)
relationsRow = c(relationsviolabilityMI, relationsconditioningMI, relationsexceptionalityMI, relationsreparabilityMI, relationsfoundationMI, relationsstrictureMI, relationsrelationsMI, relationsconstituentMI, relationscountMI)
constituentRow = c(constituentviolabilityMI, constituentconditioningMI, constituentexceptionalityMI, constituentreparabilityMI, constituentfoundationMI, constituentstrictureMI, constituentrelationsMI, constituentconstituentMI, constituentcountMI)
countRow = c(countviolabilityMI, countconditioningMI, countexceptionalityMI, countreparabilityMI, countfoundationMI, countstrictureMI, countrelationsMI, countconstituentMI, countcountMI)

miTemplates = rbind(violabilityRow, conditioningRow, exceptionalityRow, reparabilityRow, foundationRow, strictureRow, relationsRow, constituentRow, countRow)
colnames(miTemplates) = c("violabilityCol", "conditioningCol", "exceptionalityCol", "reparabilityCol", "foundationCol", "strictureCol", "relationsCol", "constituentCol", "countCol")

miReduced = aracne.a(miTemplates, .05)

mosaic(countreparability, shade=TRUE)
assoc(countreparability, shade=TRUE)
